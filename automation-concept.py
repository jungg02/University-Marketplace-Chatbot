# Core Functions 
def fetch_changes(branch):
    """Fetch latest chatbot updates"""
    changes = get_changed_files(branch)
    return store_changes(changes)
  
def update_chatbot(changes):
    """Update chatbot to latest version based on changes"""
    new_version = adopt_changes(changes)
    return new_version

def run_automated_tests(test, new_version):
    """Run updated version through test cases and edge cases"""
    if run_golden_test(test, new_version) == "passed":
        return all_tests_passed()

def build_artifact(new_version):
    """Package chatbot update as deployable artifact (Docker image)."""
    return build_docker_image(new_version)

def require_approval(artifact):
    """Policy changes need human approval (compliance/safety team)."""
    return wait_for_approval()

def rollback(last_stable_version):
    """Rollback chatbot to last stable version."""
    deploy(previous_version)

# Main Pipeline 
def chatbot_update_pipeline(branch, old_version, test):
    updates = fetch_changes(branch)
    new_version = update_chatbot(updates)

    if run_automated_tests(test, new_version):
        success("Version updated")
        return new_version
    else:
        fail("Performance deteriorated")
        perform_finetuning()

    artifact = build_artifact(new_version)

    if require_approval():
        success("Approval granted")
        return deploy_latest_version()
    else:
        fail("Update rejected")
        return abort_update()
      
    if user_feedback(artifact):
        return
    else:
        rollback(get_last_stable_version())
        fail("Deployment failed – rolling back")

    tag_release(artifact)
    succeed("Update deployed successfully")

# Run updates
if __name__ == "__main__":
    chatbot_update_pipeline(branch, old_version, test)

