# chain of responsibility
The chain of responsibility pattern is a design that involves the use of "`Task`" objects 
and "`Processor`" objects that can work on these tasks. `Processor`s can be arranged in
a number of ways, a linked-list, tree, class hierarchy, or any other structure that allows 
data to be passed from one `Processor` to another. The idea is that each `Processor` has a 
single responsibility: to handle a task. Additionally, the handling of a task is simple: 
either the `Processor` can handle it directly, or it hands it off to the next `Processor` 
in the chain to be handled in the same way.

This provides the benefits in reduced coupling and simplicity in process handling. Tasks 
are almost completely decoupled from the logic that will process them, the `Processor` 
that will handle them can introspect the `Task` to determine whether or not it can be 
handled, meaning the `Task` need to provide many, if any additional details. In my 
implementation, the only information needed from a `Task` for a `Processor` to determine 
whether or not it's processable is a name.

Process handling is simplified by no `Processor` needing to know what other `Processors` 
can handle any given task. `Processors` simply delegate the `Task` to a linked `Processor` 
and assumes it will be handled at some point. There is the added benefit of being able to
dynamically alter this chain of responsibility at runtime. Depending on how the chain is
implemented, it can be simple to add or remove `Processor`s at runtime as needed.