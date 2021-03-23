# echo bot - it repeat that the user sent
from botbuilder.core import TurnContext

class bot:
    async def turn_on(self, turn_context:TurnContext):
        await turn_context.send_activity(turn_context.activity.text)

        