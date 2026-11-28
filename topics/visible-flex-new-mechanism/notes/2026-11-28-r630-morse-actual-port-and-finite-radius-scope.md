# R630：新Morse中心的实际端口与有限径向输入

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。
这是R630新背景本身的首次实际数值输入，不复用R628的β或几何。
科学计算仅在本公开仓库Actions运行，源码有repository/run guard。

## 两个明确不同的范围

全线左正规参考采用R630的正超几何r，归一r(0)=w(r(0))=f2(0)=f3(0)=1。
取mpmath 50位，在t=exp(-X)变量上积分两个截断t上界8、12，
分别输出β中不含w²的项和含w²的项。下界t=0是全线右端，
没有把它当有限平帽；上界以后尾项未包括，两截断之差是观察而非严格余项界。
要将它用于实际双尾背景，仍需付完整尾积分和匹配连续性。

有限径向分支在右type root设r=1、ν=rX/r为.005/.02/.1/.2，
独立逆向解ν'=2ην−ν²−ρ并向右延拓。
在负曲率区ρ≥0，逆向方程νY=ν²−2ην+ρ；若
0<ε<κ=η−sqrt(η²−maxρ)，区间(0,κ]正不变，
因此负区radius ratio≤exp(κ|I|)。实际程序报告是否满足该前提。
越过左type root进入ρ<0后，ν可能穿零；实际可用正区action单独输出，
不能沿用左正规全线分支的任意长左buffer证明。

有限分支的β只积分截止中心，模态并未满足真实平尾边界条件；
字段明确为beta_core_contribution_only，不与全线β相混。
每个分支输出半径比、高度、nu、solver状态、求积误差估计及真实调用/时间成本。
这批数值用来选择可执行的真全尾输入，不作为非零β证明、闭面或reach资格。

## 固定执行输入

源码 `scripts/r630_morse_center_port_and_finite_radius_20261128.py`，
request `computations/request-r630-morse-port-20261128.json`，
workflow `.github/workflows/visible-r630-morse-port-20261128.yml`；
argv只有`--dps 50`，源码固定默认tmax=[8,12]与上述四ε。
沿用现有真实pull规则runner；先pull两库、查规则/QUEUE，再删除凭证并执行科学源码。
最长30分钟作执行资源界限，未完成输出不冒完整结果。当前只是新计算范围，未有结果。
