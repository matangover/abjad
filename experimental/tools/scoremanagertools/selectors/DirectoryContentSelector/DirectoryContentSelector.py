import os
from experimental.tools.scoremanagertools.selectors.Selector import Selector


class DirectoryContentSelector(Selector):

    ### CLASS ATTRIBUTES ###

    asset_container_paths = []
    space_delimited_lowercase_target_name = 'file'

    ### PUBLIC METHODS ###

    def list_items(self):
        from experimental.tools.scoremanagertools.proxies.DirectoryProxy import DirectoryProxy
        result = []
        for directory_path in self.asset_container_paths:
            directory_proxy = DirectoryProxy(directory_path=directory_path, session=self.session)
            result.extend(directory_proxy.list_directory(public_entries_only=True))
            if hasattr(self, 'forbidden_directory_content_names'):
                for forbidden_directory_content_name in self.forbidden_directory_content_names:
                    if forbidden_directory_content_name in result:
                        result.remove(forbidden_directory_content_name)
        return result
