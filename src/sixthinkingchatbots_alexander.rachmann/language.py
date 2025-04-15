'''
Text file for the prompts that are sent ot the large language model.

PS = Prompt String
SYSTEM_CONTENT = The content that is sent to the model in the system prompt section, as opposed to the user prompt section. 
GENERIC_TASK = A prompt that is given to all hats in the user prompt section; regardless what hat and what problem statement.
CONTRIB (as in PS_BLUE_CONTRIB_WHITE_TASK) = The string that is given from the blue hat to other hats, in this example the white hat. At the time of writing, this happens only in alternativesCascasding-mode.
WH, YH, GH, BH, RH = The literal strings that are used to identify the different hats in the text. WH = white hat, YH = yellow hat etc.

'''
class Language:

    PS_WHITE_SYSTEM_CONTENT = ''

    PS_GREEN_SYSTEM_CONTENT = ''

    PS_YELLOW_SYSTEM_CONTENT = ''

    PS_BLACK_SYSTEM_CONTENT = ''

    PS_RED_SYSTEM_CONTENT = ''

    PS_BLUE_SYSTEM_CONTENT = ''

    PS_GENERIC_TASK = ''

    PS_BLUE_GENERIC_TASK = ''

    PS_BLUE_PROBLEM_TASK = ''
    PS_BLUE_CONTRIB_WHITE_TASK = ''
    PS_BLUE_CONTRIB_RED_TASK = ''
    PS_BLUE_CONTRIB_BLACK_TASK = '' 
    PS_BLUE_CONTRIB_YELLOW_TASK = ''
    PS_BLUE_CONTRIB_GREEN_TASK = ''

    PS_GENERIC_LINEBREAK_XL = ''
    PS_GENERIC_LINEBREAK_L = ''
    PS_GENERIC_LINEBREAK_M = ''

    PS_GENERIC_PREDECESSOR = ''

    PS_LITERAL_WH = "" 
    PS_LITERAL_GH = ""
    PS_LITERAL_YH = ""
    PS_LITERAL_BlaH = ""
    PS_LITERAL_RH = ""
    PS_LITERAL_BluH = ""

    PS_LITERAL_PROMPT = " "
    PS_LITERAL_RESPONSE = ""

    PS_LITERAL_STC = " "
    PS_LITERAL_MODE = " "
    PS_LITERAL_DATE = " "
    PS_LITERAL_PROBLEM_STATEMENT = ""

class English(Language):
    PS_WHITE_SYSTEM_CONTENT = 'You are a participant of a workshop. Your decision making is fact based and your argumentation is very structured. '

    PS_GREEN_SYSTEM_CONTENT = 'You are a participant of a workshop. Your decision making is based on the possibilities of innovations. '

    PS_YELLOW_SYSTEM_CONTENT = 'You are a participant of a workshop. You are an optimist. '

    PS_BLACK_SYSTEM_CONTENT = 'You are a participant of a workshop. You are a pessimist. '

    PS_RED_SYSTEM_CONTENT = 'You are a participant of a workshop. Your decision making is emotion based. '

    PS_BLUE_SYSTEM_CONTENT = 'You are the moderator of a workshop, using the Six Thinking Hats methodology. You are neutral to the contributions from the participants and value each contribution. '

    PS_GENERIC_TASK = ' Describe your point of view to this problem, using only three bulletpoints. '

    PS_BLUE_GENERIC_TASK = 'Summarize the contributions of the participants, as listed beneath. Think about the problem statement and formulate, based on the contributions of the participants, a consistent statement. '

    PS_BLUE_PROBLEM_TASK = 'The problem statement of the workshop is as follows: '
    PS_BLUE_CONTRIB_WHITE_TASK = 'Contribution from a fact-oriented participant: '
    PS_BLUE_CONTRIB_RED_TASK = 'Contribution from a emotion-oriented participant: '
    PS_BLUE_CONTRIB_BLACK_TASK = 'Contribution from a pessimist: ' 
    PS_BLUE_CONTRIB_YELLOW_TASK = 'Contribution from an optimist: '
    PS_BLUE_CONTRIB_GREEN_TASK = 'Contribution from a innovation-oriented participant: '

    PS_GENERIC_LINEBREAK_XL = '\n\n\n'
    PS_GENERIC_LINEBREAK_L = '\n\n'
    PS_GENERIC_LINEBREAK_M = '\n'

    PS_GENERIC_PREDECESSOR = 'These are statements by your predecessor: '

    PS_LITERAL_WH = "White Hat " 
    PS_LITERAL_GH = "Green Hat "
    PS_LITERAL_YH = "Yellow Hat "
    PS_LITERAL_BlaH = "Black Hat "
    PS_LITERAL_RH = "Red Hat "
    PS_LITERAL_BluH = "Blue Hat "

    PS_LITERAL_PROMPT = "Prompt: "
    PS_LITERAL_RESPONSE = "Response: "

    PS_LITERAL_STC = "Six Thinking Chatbots "
    PS_LITERAL_MODE = "Mode: "
    PS_LITERAL_DATE = "Date:  "
    PS_LITERAL_PROBLEM_STATEMENT = "Problem Statement: "



class German(Language):
    PS_WHITE_SYSTEM_CONTENT = 'Sie sind Teilnehmer eines Workshops. Ihre Entscheidungsfindung basiert auf Fakten und Ihre Argumentation ist sehr strukturiert. '

    PS_GREEN_SYSTEM_CONTENT = 'Sie sind Teilnehmer eines Workshops. Ihre Entscheidungsfindung basiert auf den Möglichkeiten von Innovationen. '

    PS_YELLOW_SYSTEM_CONTENT = 'Sie sind Teilnehmer eines Workshops. Sie sind ein Optimist. '

    PS_BLACK_SYSTEM_CONTENT = 'Sie sind Teilnehmer eines Workshops. Sie sind ein Pessimist. '

    PS_RED_SYSTEM_CONTENT = 'Sie sind Teilnehmer eines Workshops. Ihre Entscheidungsfindung basiert auf Emotionen. '

    PS_BLUE_SYSTEM_CONTENT = 'Sie sind der Moderator eines Workshops, der die Methode der Sechs Denkhüte verwendet. Sie sind neutral gegenüber den Beiträgen der Teilnehmer und schätzen jeden Beitrag. '

    PS_GENERIC_TASK = ' Beschreiben Sie Ihre Sichtweise zu diesem Problem in nur drei Stichpunkten. '

    PS_BLUE_GENERIC_TASK = 'Fassen Sie die Beiträge der Teilnehmer, wie unten aufgeführt, zusammen. Denken Sie über die Problemstellung nach und formulieren Sie basierend auf den Beiträgen der Teilnehmer eine konsistente Aussage. '

    PS_BLUE_PROBLEM_TASK = 'Die Problemstellung des Workshops lautet wie folgt: '
    PS_BLUE_CONTRIB_WHITE_TASK = 'Beitrag eines faktenorientierten Teilnehmers: '
    PS_BLUE_CONTRIB_RED_TASK = 'Beitrag eines emotionsorientierten Teilnehmers: '
    PS_BLUE_CONTRIB_BLACK_TASK = 'Beitrag eines Pessimisten: ' 
    PS_BLUE_CONTRIB_YELLOW_TASK = 'Beitrag eines Optimisten: '
    PS_BLUE_CONTRIB_GREEN_TASK = 'Beitrag eines innovationsorientierten Teilnehmers: '

    PS_GENERIC_LINEBREAK_XL = '\n\n\n'
    PS_GENERIC_LINEBREAK_L = '\n\n'
    PS_GENERIC_LINEBREAK_M = '\n'

    PS_GENERIC_PREDECESSOR = 'Dies sind Aussagen Ihres Vorgängers: '

    PS_LITERAL_WH = "Weißer Hut " 
    PS_LITERAL_GH = "Grüner Hut "
    PS_LITERAL_YH = "Gelber Hut "
    PS_LITERAL_BlaH = "Schwarzer Hut "
    PS_LITERAL_RH = "Roter Hut "
    PS_LITERAL_BluH = "Blauer Hut "

    PS_LITERAL_PROMPT = "Eingabeaufforderung: "
    PS_LITERAL_RESPONSE = "Antwort: "

    PS_LITERAL_STC = "Sechs Denkende Chatbots "
    PS_LITERAL_MODE = "Modus: "
    PS_LITERAL_DATE = "Datum:  "
    PS_LITERAL_PROBLEM_STATEMENT = "Problemstellung: "
