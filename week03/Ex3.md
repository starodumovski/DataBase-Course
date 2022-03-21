### Part 1
- I added key attributes as a serial numbers for all element, as, in the company, they can be used for the accounting. Especially when some elements fail.
##### Cardinalities
- One computer can have as many as possible accessories.
- Laptop can have from 0.2 till 1 TB of memory for the personal documents of an employee (But the company can assume it is too much if it uses the common servers)
- Component should support a lot of software because it is more convinient to use the same component for the different softwares when it will be more efficient. (e.g. some laptops need more memory, or better video card if it is supposed to develop games)
- One computer can have 1 or 2 operating systems because sometimes 1 is not enough if (crossplatform apps are developed), but having more than 2 OSs  can lead to decreasing of the efficiency of the computer.
- Desktop can have as many as possible components
##### Description of the EERD
The EERD describes the computer systes in the company.
Namely...
The company has different **Computers** (they must have certain **operating systems**) which are either **laptops** or **desktops**.
**Desktops** can have plants of components (**Memory**, **Sound card**, **Video card** are the **Components**) which support different softwares.
**Laptops** all have **memory**, as and all **memory components** are distributed between **Laptops**.
**Computers** are sold with **Accessories**. **Accessories** are fully distributed between **Computers**, but not all **Computers** has **Accessories**.
**Accessories** is  **Keyboards**, **Monitor**, and **Mouse**.
And also **Computers** have preinstalled software.
Also we can see that **Software** is combined with **Operating system**