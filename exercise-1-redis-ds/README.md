# Redis Data Structure Comparison: Reverse Order Retrieval

This document compares different Redis data structures for storing the numbers 1–100 in a **source Redis database** and reading them in **reverse order** from a **replica database**.

---

## 1. Strings

* **Description:** Each number is stored as a separate key (`key1`, `key2`, ..., `key100`).
* **Insertion:** `SET keyX value`
* **Reverse Retrieval:** Loop from 100 → 1 and `GET` each key.
* **Pros:**

  * Simple and intuitive.
  * Easy to retrieve individual keys.
* **Cons:**

  * Creates 100 separate keys.
  * Requires a loop for reverse retrieval.
* **Use Case:** Small datasets or unique keys where ordering is not critical.

**Diagram (partial view for 1–5):**

```
key1 → 1
key2 → 2
key3 → 3
key4 → 4
key5 → 5
...
Reverse read: GET key5, key4, key3, key2, key1
```

---

## 2. List

* **Description:** All numbers are stored in a single Redis list (`numbers_list`) preserving insertion order.
* **Insertion:** `RPUSH numbers_list value`
* **Reverse Retrieval:** `LRANGE 0 -1` and reverse in application code.
* **Pros:**

  * Single key for the entire sequence.
  * Maintains insertion order.
  * Easy to reverse with `reversed()` in code.
* **Cons:**

  * Accessing a specific element by value is slower (by index only).
* **Use Case:** Sequences, queues, or stacks where order matters.

**Diagram (partial view for 1–5):**

```
numbers_list:
[1] → [2] → [3] → [4] → [5] → ... → [100]
Reverse read: [100] → [99] → ... → [1]
```

---

## 3. Hash

* **Description:** Numbers are stored as field-value pairs under one key (`numbers_hash`).
* **Insertion:** `HSET numbers_hash numX value`
* **Reverse Retrieval:** Generate field names in reverse (`num100, num99, ..., num1`) and `HMGET`.
* **Pros:**

  * Single key stores all numbers.
  * Named fields allow partial retrieval.
  * Memory-efficient for small datasets.
* **Cons:**

  * No intrinsic order; manual reverse retrieval required.
  * Slightly more complex access.
* **Use Case:** Grouped key-value data where order is not critical.

**Diagram (partial view for 1–5):**

```
numbers_hash:
num1 → 1
num2 → 2
num3 → 3
num4 → 4
num5 → 5
...
Reverse read: HMGET num100, num99, ..., num1
```

---

## 4. Sorted Set (ZSet)

* **Description:** Numbers are stored as members with their values as scores (`numbers_zset`).
* **Insertion:** `ZADD numbers_zset score member`
* **Reverse Retrieval:** `ZREVRANGE numbers_zset 0 -1`
* **Pros:**

  * Automatically maintains order.
  * Reverse retrieval is trivial with `ZREVRANGE`.
  * Ideal for ranking, leaderboards, or sequences.
* **Cons:**

  * Slightly higher memory overhead than hash for small datasets.
  * Members must be unique.
* **Use Case:** Sequences where ordering and ranking are important.

**Diagram (partial view for 1–5):**

```
numbers_zset (member:score):
"1":1
"2":2
"3":3
"4":4
"5":5
...
Reverse read: ZREVRANGE → "100", "99", ..., "1"
```

---

## ✅ Comparison Table

| Structure  | Ordering            | Single Key | Reverse Retrieval  | Memory Efficiency | Best Use Case                      |
| ---------- | ------------------- | ---------- | ------------------ | ----------------- | ---------------------------------- |
| Strings    | Manual              | No         | Manual Loop        | Moderate          | Small, unique keys                 |
| List       | Maintained          | Yes        | Easy (reversed)    | Moderate          | Sequential data, queues, stacks    |
| Hash       | Unordered           | Yes        | Manual             | High              | Grouped key-value, partial access  |
| Sorted Set | Maintained by score | Yes        | Easy (`ZREVRANGE`) | Slightly Higher   | Ranking, sequences, reverse access |

---

## ✅ Conclusion

For **reverse-order retrieval of sequential numbers**:

* **Strings**: Works, but inefficient due to multiple keys.
* **List**: **Simple and efficient for insertion and reversal**
* **Hash**: Works but requires extra effort to reverse; not ideal.
* **Sorted Set**: **Good choice** as it automatically maintains order and allows **trivial reverse retrieval** using `ZREVRANGE`. But a Overkill with memory if the only usage is to reverse the numbers.

**Recommendation:**

> Use **List** for simplicity.

---
