What was cleaned — summary of all 10 issues fixed:





|**#	Issue Found**| **Fix Applied**|
|-|-|
|1	Not\_Useful\_Column column|Dropped entirely|
|2	Address in one column|Split into Street\_Address, State, Zip\_code|
|3	Last names with junk chars (/White, ...Potter, Flenderson\_)|Stripped with regex|
|4	Phone delimiters mixed (/, \|, -, raw digits)|Normalized to NNN-NNN-NNNN|
|5	N/a phone entries|Set to None|
|6	Y/N/Yes/No inconsistency|Standardized to Yes / No|
|7	Duplicate row (CustomerID 1020 appeared twice)|Removed|
|8	Do\_Not\_Contact = Yes rows (6 removed)|Dropped — don't call them|
|9	Rows with no phone number (Samwise, Gandalf, etc.)|Dropped — uncallable|
|10	Leading/trailing spaces in names (Michael , Winger)|Stripped via .title()|









