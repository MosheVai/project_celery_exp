from my_sub_project.eval.main_eval import main_evaluation_task
from my_sub_project.collection.main_collection import main_coll_task


def collect_and_eval():
    chain = main_evaluation_task.s() | main_coll_task.s()
    chain()


if __name__ == '__main__':
    collect_and_eval()
