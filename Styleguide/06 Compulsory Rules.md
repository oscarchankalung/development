# Compulsory Rules

* Delete or comment all `console.log()` after debugging.
<!--  -->
* Resolve all errors and warnings
<!--  -->
* [Use interfaces instead of a type alias when declaring types for objects.](https://google.github.io/styleguide/tsguide.html#interfaces-vs-type-aliases)
<!--  -->
<!--  -->
* [Omit words that are obvious given a variable's type declaration.](https://testing.googleblog.com/2017/10/code-health-identifiernamingpostforworl.html)
```java
// Bad, the type tells us what these variables are:
String nameString; List<datetime> holidayDateList;
// Better:
String name; List<datetime> holidays;
```
<!--  -->
* [Omit words that are clear from the surrounding context.](https://testing.googleblog.com/2017/10/code-health-identifiernamingpostforworl.html)

```java
// Bad, repeating the context:
class AnnualHolidaySale {int annualSaleRebate; boolean promoteHolidaySale() {...}}
// Better:
class AnnualHolidaySale {int rebate; boolean promote() {...}}
```
<!--  -->
* [Names must be descriptive and clear to a new reader. Do not use abbreviations that are ambiguous or unfamiliar to readers outside your project, and do not abbreviate by deleting letters within a word.](https://google.github.io/styleguide/tsguide.html#descriptive-names)

```tsx
// Bad
style.btnContainer
// Better
style.buttonContainer
```
