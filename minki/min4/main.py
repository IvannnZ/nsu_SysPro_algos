import os
from subprocess import check_output
from subprocess import run
from sys import argv

_, git_path, first_git_commit, last_git_commit, program_for_check = argv

# git_path = "dir_for_test"
# first_git_commit = "6c5d97c"
# last_git_commit = "b1906a8"
# program_for_check = "./ultraprogram"


os.chdir(git_path)

git_log = check_output(f"git log {first_git_commit}..{last_git_commit} --oneline", shell=True).decode().splitlines()
commits = list(i.split()[0] for i in git_log)
commits.append(first_git_commit)
print('Commits:', commits)


def check_commit(commit):
    os.system(f'git checkout {commit}')
    answ = run(program_for_check, capture_output=True).returncode == 0
    os.system('git checkout -')
    return answ


count_for_check = len(commits)

left_edge = 0
right_edge = len(commits)

while right_edge - left_edge > 1:
    pivot = int((right_edge + left_edge) / 2)
    if check_commit(commits[pivot]):
        right_edge = pivot
    else:
        left_edge = pivot

print(commits[left_edge])
