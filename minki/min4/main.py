import os
from subprocess import check_output
from subprocess import run
from sys import argv

#_, git_path, first_git_commit ,last_git_commit ,program_for_check = argv


git_path = ".."

first_git_commit = ""
last_git_commit = ""

program_for_check = ("")

args = {'rep_path': git_path, 'first_commit': first_git_commit, 'latest_commit': last_git_commit,
        'command': program_for_check}

os.chdir(args['rep_path'])

os.system('git log --oneline')

git_log_command = f"git log --oneline"  # TODO сюда добавить диапазон
git_log = check_output(git_log_command, shell=True).decode().splitlines()
commits = list(i.split()[0] for i in git_log)
commits.append(args['first_commit'])

print(commits)


def check_commit(commit):
    os.system(f'git checkout {commit}')
    return run(args['command']) == 0


count_for_check = len(commits)


left_edge = 0
right_edge = len(commits)

while right_edge - left_edge > 1:
    pivot = (right_edge + left_edge)/2
    if check_commit(commits[pivot]):
        right_edge = pivot
    else:
        left_edge = pivot

print(left_edge)