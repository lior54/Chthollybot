import nextcord

from utils.utils import custom_id

VIEW_NAME = "RoleView"
class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @nextcord.ui.button(label="Test", emoji="🧪", style=nextcord.ButtonStyle.primary, custom_id=custom_id(view=VIEW_NAME, id=1061257763210149998))
    def test_button(self, button, interaction):
        interaction.response.send_message("you clicked {button.label}")