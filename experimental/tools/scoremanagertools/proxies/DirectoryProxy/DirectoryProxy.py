import os
import subprocess
from experimental.tools.scoremanagertools.proxies.FilesystemAssetProxy import FilesystemAssetProxy


class DirectoryProxy(FilesystemAssetProxy):

    ### INITIALIZER ###

    def __init__(self, directory_path=None, session=None):
        FilesystemAssetProxy.__init__(self, filesystem_path=directory_path, session=session)

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _svn_add_command(self):
        return 'cd {} && svn-add-all'.format(self.directory_path)

    ### PUBLIC METHODS ###

    def conditionally_make_empty_asset(self, is_interactive=False):
        self.print_not_yet_implemented()

    def fix(self, is_interactive=False):
        pass

    def get_filesystem_path_interactively(self):
        getter = self.io.make_getter(where=self.where())
        getter.append_string('directory path')
        result = getter.run()
        if self.session.backtrack():
            return
        self.filesystem_path = result

    def list_directory(self, public_entries_only=False):
        result = []
        if public_entries_only:
            for directory_entry in os.listdir(self.filesystem_path):
                if directory_entry[0].isalpha() and \
                    not directory_entry.endswith('.pyc'):
                    result.append(directory_entry)
        else:
            for directory_entry in os.listdir(self.filesystem_path):
                if not directory_entry.startswith('.') and \
                    not directory_entry.endswith('.pyc'):
                    result.append(directory_entry)
        return result

    def make_directory(self):
        os.mkdir(self.filesystem_path)

    def print_directory_entries(self):
        self.io.display(self.list_directory(), capitalize_first_character=False)
        self.io.display('')
        self.session.hide_next_redraw = True

    def profile(self):
        pass
