
The specification for this program is as follows,

## Specification

You are asked to build the task manager project with the use of django server.

1) A new route to show form for adding tasks. `GET /tasks`
2) A new route to add the task. `GET /add-task `
3) A new route to view completed tasks. ` GET /completed_tasks `
4) A new route to mark tasks as completed. ` GET /complete_task/<Task Index> `
5) A new route to delete the task. `GET /delete-task/<Task Index> `
6) A new route to render the all pending and completed tasks. `GET /all_tasks `

Completed tasks should no longer be visible in the existing tasks view.

You are only supposed to use in-memory variables to store data in the submission.

> Note: Please make sure your URL patterns have a trailing slash to pass the tests.

## Boilerplate code

Use the following repository as a starting point for this project: https://github.com/vigneshhari/GDC-Level-4-Milestone

To install the requirements for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Testing

Run the following command to test your application.

```bash
python manage.py test
```