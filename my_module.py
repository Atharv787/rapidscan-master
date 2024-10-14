from flask import abort

def trigger_404():
    abort(404)

# Incorrect (inside a condition)
if __name__ == "__main__":
    def contact():
        pass

# Correct
def contact():
    pass
