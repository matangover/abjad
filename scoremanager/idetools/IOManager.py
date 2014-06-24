# -*- encoding: utf-8 -*-
import abc
import os
import readline
import subprocess
import sys
import traceback
from abjad.tools import datastructuretools
from abjad.tools import stringtools
from abjad.tools import systemtools
from abjad.tools.systemtools.IOManager import IOManager


class IOManager(IOManager):
    r'''IO manager.

    ..  container:: example

        ::

            >>> score_manager = scoremanager.idetools.AbjadIDE(is_test=True)
            >>> io_manager = score_manager._session.io_manager

    '''

    ### CLASS VARAIBLES ###

    __slots__ = (
        '_client',
        '_configuration',
        '_session',
        )

    ### INITIALIZER ###

    def __init__(self, client=None, session=None):
        from scoremanager import idetools
        self._client = client
        self._configuration = idetools.Configuration()
        self._session = session

    ### SPECIAL METHODS ###

    def __repr__(self):
        r'''Gets interpreter representation of IO manager.

        ..  container:: example

            ::

                >>> io_manager
                IOManager()

        Returns string.
        '''
        return '{}()'.format(type(self).__name__)

    ### PRIVATE METHODS ###

    def _acknowledge(self):
        message = 'press any key to continue.'
        self._confirm(message=message)

    def _confirm(self, message='ok?', include_chevron=False):
        if not self._session.confirm:
            return True
        getter = self._make_getter(include_newlines=False)
        getter.append_yes_no_string(
            message,
            include_chevron=include_chevron,
            )
        result = getter._run()
        if isinstance(result, str):
            if 'yes'.startswith(result.lower()):
                return True
            if 'no'.startswith(result.lower()):
                return False

    def _controller(
        self,
        clear_terminal=False,
        consume_local_backtrack=False,
        controller=None,
        current_score_directory=None,
        is_in_confirmation_environment=False,
        on_enter_callbacks=None,
        on_exit_callbacks=None,
        ):
        from scoremanager import idetools
        return idetools.ControllerContext(
            clear_terminal=clear_terminal,
            consume_local_backtrack=consume_local_backtrack,
            controller=controller,
            current_score_directory=current_score_directory,
            is_in_confirmation_environment=is_in_confirmation_environment,
            on_enter_callbacks=on_enter_callbacks,
            on_exit_callbacks=on_exit_callbacks,
            )

    def _display(self, lines, capitalize=True, is_menu=False):
        assert isinstance(lines, (str, list))
        if not self._session.display:
            return
        if isinstance(lines, str):
            lines = [lines]
        if capitalize:
            lines = [stringtools.capitalize_start(_) for _ in lines ]
        if lines:
            self._session.transcript._append_entry(lines, is_menu=is_menu)
        for line in lines:
            print(line)

    def _display_not_yet_implemented(self):
        message = 'not yet implemented.'
        self._display(message)

    @staticmethod
    def _get_greatest_version_number(version_directory):
        if not os.path.isdir(version_directory):
            return 0
        greatest_number = 0
        for entry in os.listdir(version_directory):
            base_name, extension = os.path.splitext(entry)
            number = 0
            try:
                number = int(base_name[-4:])
            except ValueError:
                pass
            if greatest_number < number:
                greatest_number = number
        return greatest_number

    @staticmethod
    def _get_one_line_menu_summary(expr):
        if isinstance(expr, (type, abc.ABCMeta)):
            return expr.__name__
        elif getattr(expr, '_one_line_menu_summary', None):
            return expr._one_line_menu_summary
        elif isinstance(expr, str):
            return expr
        else:
            return repr(expr)

    def _handle_input(
        self,
        message,
        default_value=None,
        include_chevron=True,
        include_newline=False,
        prompt_character='>',
        capitalize_prompt=True,
        ):
        r'''Handles user input.
        Appends user input to command history.
        Appends user input to IO transcript.
        Returns command selected by user.
        '''
        if default_value in (None, 'None'):
            default_value = ''
        readline.set_startup_hook(lambda: readline.insert_text(default_value))
        found_default_token = False
        # TODO: replace try-finally with startup hook context manager
        try:
            if capitalize_prompt:
                message = stringtools.capitalize_start(message)
            if include_chevron:
                message = message + prompt_character + ' '
            else:
                message = message + ' '
            if not self._session.pending_input:
                was_pending_input = False
                if sys.version_info[0] == 2:
                    input_ = raw_input(message)
                else:
                    input_ = input(message)
                if include_newline:
                    if not input_ == 'help':
                        print('')
            else:
                was_pending_input = True
                input_ = self._pop_from_pending_input()
                if input_ == '<return>':
                    found_default_token = True
            if not found_default_token:
                self._session.command_history.append(input_)
            if input_ == '.':
                last_semantic_command = self._session.last_semantic_command
                input_ = last_semantic_command
            if found_default_token:
                menu_chunk = [message.strip()]
                if include_newline:
                    if not input_ == 'help':
                        menu_chunk.append('')
                self._session.transcript._append_entry(menu_chunk)
                if was_pending_input:
                    for string in menu_chunk:
                        print string
                menu_chunk = ['> ']
                if include_newline:
                    if not input_ == 'help':
                        menu_chunk.append('')
                self._session.transcript._append_entry(menu_chunk)
                if was_pending_input:
                    for string in menu_chunk:
                        print string
            else:
                menu_chunk = []
                menu_chunk.append('{}{}'.format(message, input_))
                if include_newline:
                    if not input_ == 'help':
                        menu_chunk.append('')
                self._session.transcript._append_entry(menu_chunk)
                if was_pending_input:
                    for string in menu_chunk:
                        print string
            return input_
        finally:
            readline.set_startup_hook()

    def _invoke_shell(self, statement):
        lines = []
        prompt = True
        process = subprocess.Popen(
            statement,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            )
        try:
            lines = [str(x) for x in process.stdout.readlines()]
        except:
            lines.append('expression not executable.')
        lines = lines or []
        lines = [_.strip() for _ in lines]
        self._display(lines, capitalize=False)

    @staticmethod
    def _list_directory(path, public_entries_only=False):
        result = []
        if not path or not os.path.exists(path):
            return result
        if public_entries_only:
            for directory_entry in sorted(os.listdir(path)):
                if directory_entry[0].isalpha():
                    if not directory_entry.endswith('.pyc'):
                        if not directory_entry in ('test',):
                            result.append(directory_entry)
        else:
            for directory_entry in sorted(os.listdir(path)):
                if not directory_entry.startswith('.'):
                    if not directory_entry.endswith('.pyc'):
                        result.append(directory_entry)
        return result

    def _make_autoeditor(
        self, 
        allow_item_edit=True,
        breadcrumb=None,
        target=None,
        ):
        from scoremanager import idetools
        kwargs = {
            'allow_item_edit': allow_item_edit,
            'breadcrumb': breadcrumb,
            'session': self._session,
            'target': target,
            }
        if isinstance(target, (dict, datastructuretools.TypedOrderedDict)):
            class_ = idetools.DictionaryAutoeditor
        elif isinstance(target, (list, datastructuretools.TypedCollection)):
            class_ = idetools.ListAutoeditor
        else:
            class_ = idetools.Autoeditor
            kwargs.pop('allow_item_edit')
        autoeditor = class_(**kwargs)
        return autoeditor

    def _make_getter(
        self,
        allow_none=False,
        include_chevron=True,
        include_newlines=False,
        ):
        from scoremanager import idetools
        getter = idetools.UserInputGetter(
            session=self._session,
            allow_none=allow_none,
            include_chevron=include_chevron,
            include_newlines=include_newlines,
            )
        return getter

    def _make_interaction(
        self, 
        confirm=True, 
        display=True, 
        dry_run=False, 
        task=True,
        ):
        from scoremanager import idetools
        return idetools.Interaction(
            confirm=confirm,
            controller=self.client, 
            display=display,
            dry_run=dry_run,
            task=task,
            )

    def _make_menu(
        self,
        breadcrumb_callback=None,
        name=None,
        prompt_character='>',
        subtitle=None,
        ):
        from scoremanager import idetools
        return idetools.Menu(
            breadcrumb_callback=breadcrumb_callback,
            name=name,
            prompt_character=prompt_character,
            session=self._session,
            subtitle=subtitle,
            )

    def _make_package_manager(self, path):
        from scoremanager import idetools
        return idetools.PackageManager(
            path=path,
            session=self._session,
            )

    def _make_selector(
        self,
        breadcrumb=None,
        is_ranged=False,
        items=None,
        ):
        from scoremanager import idetools
        return idetools.Selector(
            breadcrumb=breadcrumb,
            is_ranged=is_ranged,
            items=items,
            session=self._session,
            )

    def _make_tab(self, n=1):
        return 4 * n * ' '

    def _pop_from_pending_input(self):
        self._session._last_command_was_composite = False
        if self._session.pending_input is None:
            return None
        elif self._session._pending_input == '':
            self._session._pending_input = None
            return None
        elif self._session.pending_input.startswith('{{'):
            index = self._session.pending_input.find('}}')
            input_ = self._session.pending_input[2:index]
            pending_input = self._session.pending_input[index+2:]
            pending_input = pending_input.strip()
            self._session._last_command_was_composite = True
        else:
            input_parts = self._session.pending_input.split(' ')
            first_parts, rest_parts = [], []
            for i, part in enumerate(input_parts):
                if not part.endswith((',', '-')):
                    break
            first_parts = input_parts[:i+1]
            rest_parts = input_parts[i+1:]
            input_ = ' '.join(first_parts)
            pending_input = ' '.join(rest_parts)
        input_ = input_.replace('~', ' ')
        self._session._pending_input = pending_input
        return input_

    def _silent(self):
        from scoremanager import idetools
        return idetools.Interaction(
            confirm=False,
            controller=self.client,
            display=False,
            dry_run=False,
            task=False,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def client(self):
        r'''Gets client of IO manager.

        Returns score manager object.
        '''
        return self._client

    @property
    def selector(self):
        r'''Gets dummy selector.

        Use for access to selector make methods.

        Returns selector.
        '''
        from scoremanager import idetools
        return idetools.Selector(session=self._session)

    ### PUBLIC METHODS ###

    def check_file(self, path):
        r'''Checks file `path`.

        Silently interprets file `path` with Python or LilyPond.

        Returns stderr lines; nonempty list means interpretation raised errors.
        '''
        with self._silent():
            stdout_lines, stderr_lines = self.interpret_file(path)
        return stderr_lines

    def edit(self, path, line_number=None):
        r'''Edits file `path`.

        Opens at `line_number` when `line_number` is set.

        Opens at first line when `line_number` is not set.

        Returns none.
        '''
        if not os.path.isfile(path):
            message = 'file not found: {}.'
            message = message.format(path)
            self._display(message)
            return
        if line_number is None:
            command = 'vim + {}'.format(path)
        else:
            command = 'vim +{} {}'.format(line_number, path)
        self._session._attempted_to_open_file = True
        if self._session.is_test:
            return
        self.spawn_subprocess(command)

    def execute_file(self, path=None, attribute_names=None):
        r'''Executes file `path`.

        Returns `attribute_names` from file.
        '''
        assert path is not None
        assert isinstance(attribute_names, tuple)
        if not os.path.isfile(path):
            return
        with open(path, 'r') as file_pointer:
            file_contents_string = file_pointer.read()
        try:
            exec(file_contents_string)
        except:
            message = 'Exception raised in {}.'
            message = message.format(path)
            # use print instead of display
            # to force to terminal even when called in silent context
            print(message)
            traceback.print_exc()
            return 'corrupt'
        result = []
        for name in attribute_names:
            if name in locals():
                result.append(locals()[name])
            else:
                result.append(None)
        result = tuple(result)
        return result

    def interpret_file(self, path):
        r'''Invokes Python or LilyPond on `path`.

        Displays any in-file messaging during interpretation.
        '''
        if not os.path.exists(path):
            message = 'file not found: {}'.format(path)
            self._display(message)
            return False
        _, extension = os.path.splitext(path)
        if extension == '.py':
            command = 'python {}'.format(path)
        elif extension == '.ly':
            command = 'lilypond {}'.format(path)
        else:
            message = 'can not interpret {}.'.format(path)
            raise Exception(message)
        directory = os.path.dirname(path)
        directory = systemtools.TemporaryDirectoryChange(directory)
        with directory:
            #result = self.spawn_subprocess(command)
            #process = self.make_subprocess(command)
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                )
        stdout_lines = []
        for stdout_line in process.stdout.readlines():
            stdout_line = str(stdout_line)
            stdout_line = stdout_line.strip()
            stdout_lines.append(stdout_line)
        self._display(stdout_lines, capitalize=False)
        stderr_lines = []
        for stderr_line in process.stderr.readlines():
            stderr_line = str(stderr_line)
            stderr_line = stderr_line.strip()
            stderr_lines.append(stderr_line)
        self._display(stderr_lines, capitalize=False)
        message = 'interpreted {}.'.format(path)
        self._display(message)
        #return result
        return stdout_lines, stderr_lines

    def open_file(self, path):
        r'''Opens file `path`.

        Also works when `path` is a list.

        Returns none.
        '''
        if not isinstance(path, list) and not os.path.isfile(path):
            return
        if (isinstance(path, list) and
            all(_.endswith('.pdf') for _ in path)):
            paths = ' '.join(path)
            command = 'open {}'.format(paths)
        elif (isinstance(path, list) and
            all(_.endswith('.mp3') for _ in path)):
            paths = ' '.join(path)
            command = 'open {}'.format(paths)
        elif (isinstance(path, list) and
            all(_.endswith('.aif') for _ in path)):
            paths = ' '.join(path)
            command = 'open {}'.format(paths)
        elif isinstance(path, list):
            paths = path
            paths = ' '.join(paths)
            command = 'vim {}'.format(paths)
        elif path.endswith('.pdf'):
            command = 'open {}'.format(path)
        elif path.endswith('.mp3'):
            command = 'open {}'.format(path)
        elif path.endswith('.aif'):
            command = 'open {}'.format(path)
        else:
            command = 'vim {}'.format(path)
        self._session._attempted_to_open_file = True
        if self._session.is_test:
            return
        self.spawn_subprocess(command)

    def run_command(self, command, capitalize=True, messages_only=False):
        r'''Makes subprocess with `command` and then runs and displays
        output of subprocess.

        Returns none.
        '''
        process = self.make_subprocess(command)
        lines = [str(line).strip() for line in process.stdout.readlines()]
        if not lines:
            return
        if messages_only:
            return lines
        self._display(lines, capitalize=capitalize)

    def run_lilypond(self, path):
        r'''Runs LilyPond on file `path`.

        Returns none.
        '''
        if self.find_executable('lily'):
            executable = 'lily'
        elif self.find_executable('lilypond'):
            executable = 'lilypond'
        else:
            message = 'cannot find LilyPond executable.'
            raise ValueError(message)
        command = '{} {}'.format(
            executable,
            path,
            )
        input_directory = os.path.dirname(path)
        with systemtools.TemporaryDirectoryChange(input_directory):
            self.spawn_subprocess(command)

    def write(self, path, string):
        r'''Writes `string` to `path`.

        Returns none.
        '''
        with open(path, 'w') as file_pointer:
            file_pointer.write(string)

    def write_stub(self, path):
        r'''Writes Unicode directive to otherwise empty file at `path`.

        Returns none.
        '''
        with open(path, 'w') as file_pointer:
            file_pointer.write(self._configuration.unicode_directive)