from tethys_sdk.base import TethysAppBase, url_map_maker


class Myfirstapp(TethysAppBase):
    """
    Tethys app class for Myfirstapp.
    """

    name = 'Myfirstapp'
    index = 'myfirstapp:home'
    icon = 'myfirstapp/images/icon.gif'
    package = 'myfirstapp'
    root_url = 'myfirstapp'
    color = '#096247'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='myfirstapp',
                controller='myfirstapp.controllers.home'
            ),
        )

        return url_maps
