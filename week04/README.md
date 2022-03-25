### Exercise 1
1. **Find the names of suppliers who supply some red part.**
$\pi_{sname}((\sigma_{color="Red"}(Parts)$ ᛞ $Catalog)$ ᛞ $Suppliers))$
2. **Find the sids of suppliers who supply some red or green part**
$\pi_{sid}((\sigma_{color="Red"}(Parts)$U $\sigma_{color="Green"}(Parts))$ ᛞ $Catalog)$
3. **Find the sids of suppliers who supply some red part or are at 221 Packer Street**
$\pi_{sid}((\sigma_{color=Red}(Parts)$ ᛞ $Catalog)$ ᛞ $Suppliers))$ U $\pi_{sid}(\sigma_{street="221 Packer Street"}(Suppliers))$
4.  **Find the sids of suppliers who supply some red part and some green part.**
$\pi_{sid}(\sigma_{color="Red"}(Parts)$ ᛞ $Catalog)$ + $\pi_{sid}(\sigma_{color="Green"}(Parts)$ ᛞ $Catalog)$
6. **Find the sids of suppliers who supply every part.**
$R1$ <- $\pi_{sid,pid}(Catalog)$
$R2$ <- $\pi_{sid}(Suppliers)$ x $\pi_{pid}(Parts)$
$R3$ <- $\pi_{sid}$($R2$/$R1$)
**result** <- $\pi_{sid}(Catalog)$/$R3$
8. **Find the sids of suppliers who supply every red part.** 
$R1$ <- $\sigma_{color='Red'}(Parts)$
$R2$ <- $\pi_{sid}(Suppliers)$ x $\pi_{pid}(R1)$ 
$R3$ <- $\pi_{sid, pid}(Catalog)/R2$ 
**result** <- $\pi_{sid}(Catalog)/\pi_{sid}(R3)$ 
10.  **Find the sids of suppliers who supply every red or green part.** 
$R1$ <- $\sigma_{color='Red'}(Parts)$
$R2$ <- $\pi_{sid}(Suppliers)$ x $\pi_{pid}(R1)$ 
$R3$ <- $\pi_{sid, pid}(Catalog)/R2$ 
EVERYRED <- $\pi_{sid}(Catalog)/\pi_{sid}(R3)$ 
GREEN <- $\pi_{sid}((\sigma_{colour="green"}(Parts)$ ᛞ $Catalog)$ ᛞ $Suppliers))$
**result** <- (EVERYRED) U (GREEN)
12. **Find the sids of suppliers who supply every red part or supply every green part.** 
$R1$ <- $\sigma_{color='Red'}(Parts)$
$R2$ <- $\pi_{sid}(Suppliers)$ x $\pi_{pid}(R1)$ 
$R3$ <- $\pi_{sid, pid}(Catalog)/R2$ 
EVERYR <- $\pi_{sid}(Catalog)$/$\pi_{sid}(R3)$ 
$G1$ <- $\sigma_{color='Green'}(Parts)$
$G2$ <- $\pi_{sid}(Suppliers)$ x $\pi_{pid}(G1)$ 
$G3$ <- $\pi_{sid, pid}(Catalog)/G2$ 
EVERYG <- $\pi_{sid}(Catalog)/\pi_{sid}(G3)$ 
**result** <- (EVERYR) U (EVERYG)
14. **Find pairs of sids such that the supplier with the first sid charges more for some part than the supplier with the second sid.** 
$LeftSide$ <- $\pi_{sid, pid, cost}(Catalog)$
$psid1$->$sid(LeftSide)$
$ppid1$->$pid(LeftSide)$
$pcost1$->$cost(LeftSide)$
$RightSide$ <- $\pi_{sid, pid, cost}(Catalog)$
$psid2$->$sid(RightSide)$
$ppid2$->$pid(RightSide)$
$pcost2$->$cost(RightSide)$
$temp$ <- $LeftSide$ ᛞ$_{cost1 > cost2}$ $RightSide$
**result** <- $\pi_{sid1, sid2}(temp)$
18. **Find the pids of parts supplied by at least two different suppliers**
$p(R1,Catalog)$
$p(R2, Catalog)$
**result** <- $\pi_{pid}(\sigma_{R1.sid \;!=\; R2.sid\;and\;R1.pid \;=\; R2.pid}(R1$ x $R2))$

### Exercise 2
1. It computes the **sname**s of the **Suppliers** who supplied **red** **Parts** with **cost** less than 100.
2. It computes the **sname**s of **Suppliers** who supplied **red** and **green** **Parts** with the **cost** less than 100 for each part.
3. It computes the **sid**s of **Suppliers** who supplied **red** and **green** **Parts** with **cost** less than 100 for each part
4. It computes the **sname**s of Suppliers who supplied **red** and **green** **Parts** with the **cost** less than 100 for each part.