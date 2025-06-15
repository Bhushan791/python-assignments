# 🦁 Zoo Management System

A simple Zoo Management CLI application built using Object-Oriented Programming (OOP) principles in Python.

## 📌 Description

This project simulates a zoo system where users can manage different animals, their feeding schedules, and enclosures. It demonstrates core OOP pillars: **Encapsulation, Inheritance, Polymorphism,** and **Abstraction**.

## ✅ Key Features

- Add new animals with specific attributes (name, species, age)
- Assign enclosures and schedule feeding times
- Feed animals and hear their sounds (via polymorphism)
- Easy to extend by creating new animal subclasses
- Abstract base class ensures consistency across animal types

## 🚀 OOP Concepts Used

| OOP Concept   | Implementation Example |
|--------------|------------------------|
| **Encapsulation** | Private attributes with getter/setter methods |
| **Inheritance**   | `Lion`, `Elephant`, `Parrot` inherit from base `Animal` class |
| **Polymorphism**  | `make_sound()` behaves differently across animal types |
| **Abstraction**   | Abstract methods in the base class force implementation in subclasses |

## 🛠 How to Run

cmd:
python Zoo_Management/OOP_Zoo_Management.py