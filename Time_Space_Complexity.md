## Time & Space Complexity Cheat Sheet

### Core Asymptotic Notation

- `O(f(n))`: upper bound (worst/ceil).
- `Omega(f(n))`: lower bound (best/floor).
- `Theta(f(n))`: tight bound (both upper and lower).
- `o(f(n))`: strictly smaller order; `omega(f(n))`: strictly larger order.

### Growth Landmarks (slowest -> fastest blow-up)

`1 < log n < sqrt(n) < n < n log n < n^2 < n^3 < 2^n < n!`

### Common Patterns

- Loops: cost = iterations \* body cost. Nested loops multiply.
- Sequential steps: add costs. Dominant term rules overall (`n + n^2` -> `n^2`).
- Divide & conquer: express recurrence and solve (often Master Theorem).
- Amortized arrays/vecs: occasional resize is O(1) amortized per push.
- Hash table ops: O(1) expected, O(n) worst (pathological collisions).
- Balanced BST / heap ops: O(log n); array scan: O(n).

### Master Theorem Quick Use

Recurrence: `T(n) = a T(n/b) + f(n)`, with `a >= 1`, `b > 1`.

- Compare `f(n)` to `n^{log_b a}`.
- If `f(n) = O(n^{log_b a - epsilon})`: `T(n) = Theta(n^{log_b a})`.
- If `f(n) = Theta(n^{log_b a} log^k n)`: `T(n) = Theta(n^{log_b a} log^{k+1} n)`.
- If `f(n) = Omega(n^{log_b a + epsilon})` and regularity holds: `T(n) = Theta(f(n))`.

### Logarithm Reminders

- Bases change by constant: `log_k n = (log n)/(log k)`.
- Tree/heap height with branching factor `b`: `~ log_b n`.
- Repeated halving/doubling processes usually give `log n` steps.

### Typical Algorithm Costs

- Binary search: O(log n) time, O(1) space.
- Merge sort: O(n log n) time, O(n) extra space.
- Quick sort (good pivot): O(n log n) avg, O(n) stack; worst O(n^2).
- Heap sort: O(n log n) time, O(1) extra space.
- BFS/DFS (adjacency list): O(V + E) time, O(V) space for queue/stack + visited.
- Dijkstra (binary heap): O((V + E) log V) time, O(V + E) space.
- Union-Find (path compression + union by rank): inverse-Ackermann ~ O(1) amortized.

### Data Structure Ops (Time / Space)

| Structure                     | Access      | Search   | Insert                | Delete                   | Extra Space          |
| ----------------------------- | ----------- | -------- | --------------------- | ------------------------ | -------------------- |
| Static array                  | O(1)        | O(n)     | O(n)                  | O(n)                     | O(1)                 |
| Dynamic array (amortized)     | O(1)        | O(n)     | O(1)                  | O(n)                     | O(n) total           |
| Singly linked list            | O(n)        | O(n)     | O(1) head / O(n) tail | O(1) head / O(n) mid     | O(n)                 |
| Doubly linked list            | O(n)        | O(n)     | O(1) with pointer     | O(1) with pointer        | O(n)                 |
| Stack / Queue (array or list) | O(1)        | O(n)     | O(1)                  | O(1)                     | O(n)                 |
| Hash table (expected)         | N/A         | O(1)     | O(1)                  | O(1)                     | O(n)                 |
| Hash table (worst)            | N/A         | O(n)     | O(n)                  | O(n)                     | O(n)                 |
| Balanced BST (AVL/Red-Black)  | O(log n)    | O(log n) | O(log n)              | O(log n)                 | O(n)                 |
| Heap (binary)                 | O(1) top    | O(n)     | O(log n) push         | O(log n) pop             | O(n)                 |
| Trie (per key length k)       | O(k)        | O(k)     | O(k)                  | O(k)                     | O(alphabet \* nodes) |
| Graph (adj list)              | O(1) vertex | O(V + E) | O(1) add edge         | O(1) rm edge (if stored) | O(V + E)             |

### Space Complexity Basics

- Count extra memory beyond input (auxiliary space).
- Iterative algorithms often O(1) extra; recursion adds call stack depth.
- In-place means O(1) or O(log n) extra, not counting input storage.
- Data structure overhead matters: pointers, object headers, padding.

### Recursion Stack Costs

- Depth \* (locals + return address). Tail recursion can be optimized to O(1) space in some languages; assume not unless specified.
- Example depths: binary recursion on size `n` usually depth `log n`; linear recursion depth `n`.

### Amortized Analysis (Brief)

- Aggregate: total cost over `m` ops divided by `m` (e.g., dynamic array growth).
- Accounting: assign credits to cheap ops to pay for future expensive ones.
- Potential method: define potential function `Phi` so that amortized cost = actual cost + Delta `Phi`.

### When to State Bounds

- Mention best/avg/worst if they differ (e.g., quicksort, hashing).
- Include space alongside time for clarity.
- For graphs, specify representation (matrix vs list) and edge weights assumptions.

### Quick Checklist When Analyzing

- Identify dominant loops/recursions; write recurrence if divide-and-conquer.
- Check data structure operations: are they amortized or worst-case?
- Account for input size variables separately if multiple dimensions (n, m, V, E).
- State auxiliary space and note recursion depth.
- Prefer tight `Theta` when you can justify; use `O` when only upper bound is clear.

### Micro-Examples

- Two nested loops up to `n`: `for i in range(n): for j in range(n): ...` -> O(n^2).
- Outer `n`, inner `log n`: total O(n log n).
- Halving loop: `while n > 1: n //= 2` -> O(log n) iterations.
- Merge two sorted arrays of total length `n`: O(n) time, O(1) extra.

### Space vs Time Trade-offs

- Extra indexing/lookup tables can drop time (e.g., memoization DP) at cost of space.
- In-place strategies save space but can complicate time or stability (e.g., in-place merge).
- Caching/compression can alter both; always state assumptions.

### Handy Bounds

- Harmonic series: sum\_{k=1..n} 1/k = Theta(log n).
- Geometric series: sum\_{i=0..k} r^i = O(1) if |r|<1; otherwise Theta(r^k).
- Binary lifting/jump tables: preprocess O(n log n), query O(log n) typical.

### Notation Hygiene

- Use clear variable names for sizes: `n` (elements), `m` (edges), `V`/`E`, `k` (key length), `W` (word size).
- Avoid mixing units: if costs depend on value magnitude (e.g., counting sort), state range `K`.

### Practical Tips

- Benchmark constants matter in practice even if asymptotics match.
- Watch cache friendliness: contiguous memory often speeds real-world performance.
- For interview settings, say the bound, then briefly justify in 1-2 sentences.
