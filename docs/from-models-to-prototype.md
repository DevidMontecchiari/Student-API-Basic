# From your models to a working API

Use your project scenario, UML diagrams and sample JSON to adapt the small Student API. Work on one useful operation at a time, check its behaviour, then extend it. This guide supports the existing assignment; it does not add deliverables or require every CRUD operation.

[Setup and Python refresher](../README.md) | [Starter code](../main.py)

## 1. Run the unchanged example

Open your own copy using the [README instructions](../README.md#1-run-your-own-copy). In its terminal, enter:

```sh
python run.py
```

Open `/docs` and try `GET /students/1002`, `/students/9999` and `/students/abc`. Expect 200, 404 and 422 respectively. Find the route, file loader, comparison and return in `main.py` before changing them. [Startup help](../README.md#quick-startup-checks).

**Checkpoint:** you can explain how one request retrieves a JSON record. Save a working copy or commit before adapting it.

## 2. Select a small part of your scenario

Keep your use case description, class diagram, data model and sample JSON beside the code. Choose one information need from the scenario. For example:

> A student wants to view a course's details before deciding whether to register.

Start with **view course details**. Registration changes data and can be added separately. Identify the actor, goal, input, expected output and what happens when the requested course does not exist.

A user story describes the need. The API operation supplies part of the behaviour needed to meet it; one use case can require several operations. A use case actor is not automatically a data entity or an implemented login role.

**Checkpoint:** describe the selected operation in one sentence and show where it belongs in your scenario.

## 3. Map the model to data and behaviour

For the school example, the model provides `Course` with `course_id: String` and `title: String`. Decide how those attributes appear in the JSON and the request:

| Model or scenario decision | Example implementation decision |
| --- | --- |
| Course identity | `course_id`, for example `"IS101"` |
| Course title | `title`, for example `"Information Systems"` |
| Collection of course records | An array in `data/courses.json` |
| Read all courses | `GET /courses` |
| Read one course | `GET /courses/{course_id}` with `course_id: str` |
| Course does not exist | 404 with `Course not found` |

Use the same mapping for your own entity. Resolve inconsistent names and types before coding. A JSON string is quoted; a JSON number is not. The starter's JSON loader does not validate your UML attributes, required fields or relationships.

A UML class can guide the data structure even when this small implementation uses dictionaries. The [full school reference](https://github.com/DevidMontecchiari/School-IS-api) separately illustrates Python classes and objects.

**Checkpoint:** each sample field has a meaning in your model, and each requested value has an agreed type.

## 4. Adapt the read operations

In your own starter copy, first make the course example or apply these changes directly to your selected project entity.

1. Create `data/courses.json` with the records below. Keep the original student file until the new routes work.
2. In `main.py`, change `STUDENTS_FILE` to `COURSES_FILE` everywhere and point it to `data/courses.json`.
3. Rename `load_students` to `load_courses`, including both calls. Keep its JSON-reading behaviour.
4. Change `/students` and `list_students` to `/courses` and `list_courses`.
5. Change the other route to `/courses/{course_id}` and the function signature to `get_course(course_id: str)`. The name inside `{...}` must match the parameter name.
6. Rename the local variables to `courses` and `course`. Compare `course["course_id"] == course_id`, then return `course`. Keep the 404 **after** the loop and update its message.
7. Update the application's title and welcome message to match your case. Leave `run.py` and the environment setup unchanged.

```json
[
  {"course_id": "IS101", "title": "Information Systems"},
  {"course_id": "DB101", "title": "Databases"}
]
```

Save, wait for the application to reload, then refresh `/docs`. If it stopped with an error, read the terminal, correct the indicated line and restart with `python run.py`.

## 5. Compare expected and actual results

Write down the expected result before executing each request:

| Request or action | Expected result for this example |
| --- | --- |
| `GET /courses` | 200, both course records |
| `GET /courses/DB101` | 200, the second record; checks that the search continues past the first |
| `GET /courses/UNKNOWN` | 404, no matching course |
| `GET /courses/abc` | 404, because `abc` is a valid string but has no record |
| Edit a course title in the JSON, save, then GET it again | Updated title; restore it after checking |

Unlike `student_id: int`, `course_id: str` does not reject `abc` as the wrong type. A rule about the *format* of a course code would need an additional explicit check.

Trace the result back through the route, loader, comparison and response. If the implementation and model disagree, decide which needs correction and keep both consistent. An HTTP 200 alone does not prove the returned data is correct.

## 6. Extend only what your scenario needs

Once the read operations work, choose the next relevant change. Basic create, read, update and delete operations are sufficient building blocks; you do not need a complex workflow engine.

For **register for a course**, the school model suggests a new Enrolment record:

```json
{"student_id": 1002, "course_id": "DB101", "grade": null}
```

The operation would check that the student and course exist, reject an existing enrolment for the same pair, create the record and save it. Check the result with a read request; repeat the registration to check that it does not create a duplicate. Translate relevant associations and constraints into checks: JSON alone does not enforce them.

The [school registration example](https://github.com/DevidMontecchiari/School-IS-api/blob/main/registration_demo.py) demonstrates this as a separate command-line program. It is **not** a POST endpoint in the starter. Returning a dictionary does not save it, and editing a JSON file manually is not an API write. Keep a backup before experimenting with writes.

## 7. Prepare the coaching discussion

Bring your updated models, sample JSON, implementation progress and report draft as described in Moodle. Be ready to demonstrate one request and explain how its input, output and rules follow from your design. Record what works, what remains incomplete and a specific question where you need help. A finished application is not expected for coaching.

If you use AI, give it the relevant model fragment, scenario and JSON, and ask for one small change at a time. For example:

> Here are our scenario, class/data model and sample JSON. We want to implement only [selected operation] in this starter. First identify the relevant attributes, ID types, inputs, outputs and error cases. Flag inconsistencies or missing decisions instead of inventing fields. Then propose the smallest code change and explain how to check it.

Review and run the change yourself. You should be able to explain why it matches the model and show a successful request and a relevant failure case.

[Back to the starter README](../README.md)
