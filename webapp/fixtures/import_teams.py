from webapp.models import Team

a_file = open('./webapp/fixtures/teams.txt')
a = a_file.read()
b = a.split('\n')
for team in b:
     t = Team(team_name=team)
     t.save()

