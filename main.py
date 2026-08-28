from agents.design_agent import DesignAgent
from agents.implementation_agent import ImplementationAgent
from agents.requirements_agent import RequirementsAgent
from agents.review_agent import ReviewAgent
from core.orchestrator import SequentialOrchestrator
from core.state import ProjectState


def read_user_request(path="input.txt") -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read().strip()


def main():
    user_request = read_user_request()
    state = ProjectState(user_request=user_request)

    agents = [
        RequirementsAgent(),
        DesignAgent(),
        ImplementationAgent(),
        ReviewAgent(),
    ]

    orchestrator = SequentialOrchestrator(agents)
    final_state = orchestrator.run(state)

    print("\n=== Final Output ===")
    print(final_state.final_output)
    print("\nStep outputs were saved under the outputs/ folder.")


if __name__ == "__main__":
    main()
