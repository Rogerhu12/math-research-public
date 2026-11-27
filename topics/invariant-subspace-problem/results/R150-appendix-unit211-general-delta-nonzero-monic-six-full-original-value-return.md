# R150：一般两线行列式非零图的完整原值六维返回

**状态：已证明并实际完整返回。** 在当前一般 LS 图、原两线行列式非零时，原两矩、P1 和 N4(V) 唯一恢复原值与 Gram；全部剩余原均值、N1 和两个 singleton 的个别 N/P 方程已实际返回为八条 T 次数至多五的必要式。在保留全部原非零条件的同一点，这些式子与本节列出的原方程双向等价。没有除以 Phi，没有求 D 或行列式因子的有限代数范数逆，也没有判空当前图。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 原图和精确恢复

沿用[一般共同分母与首一六次原恢复](R150-appendix-unit211-general-delta-nonzero-common-denominator-and-monic-T-six-original-reconstruction.md)的全部定义和已付权图。置

$$
d=1-Q,\quad m=u-\ell,\quad V_2=2u-\ell Q,\quad
M=\ell V_2-u^2=\ell^2d-m^2,\quad bc=M/(4d),
$$
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A-T^2,\quad n_s=\ell B-AT,\quad n_z=TB-A^2,
\quad K=\ell^2B-3\ell TA+2T^3,
$$
$$
Z=u n_s-2TD,\qquad S_n=n_s+(3-2\lambda)D.
$$

这里的 T 是原加权值；小写 t 是原 Gram 配对，二者不混用。原点的 D 非零，且 ell、m、d、M 等所用权分母均已支付。原两矩在同图等价于

$$
F_6=MK^2-4m^2D^3=0,\qquad
v_0=n_s/(2D),\quad v_1=-K/(2mD),\quad
\zeta=Z/(2mD).
$$

原点的 S=S_n/D、z=n_z/D、s=-v1 随同保留。F6 的 T 六次头是 4ell²d，属于已付权单位。因此按 F6 首一化做多项式余式，不删去任何 T 首项零分支。

再设

$$
T_0=V_2-2u^2,\ J=2u(1-u)+\ell Q,\ 
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad P_f=T_0(J-Q),
\quad G=\lambda P_{02}-(1-u)T_0,\quad w=\lambda-1-T.
$$

前稿已给出整式 Pc、NF4、NC4、E、Fn、Tn，并逐项核验

$$
P_f F_n+\Phi T_n+4EP_c=0,\qquad
N_{F4}F_n+2S_nZT_n+4EN_{C4}=0.
$$

此处复用这些确切整式，原两线的行列式恰为

$$
-\frac{bcQ\,E}{mD^2}.
$$

所以当前图准确为 E≠0；同点唯一恢复

$$
f=F_n/(4E),\qquad t=T_n/(4bcQE).
$$

全程没有 Phi 的逆。E=0 整图继续由独立 W 路线处理；不把本图的可逆性施于它。

## 2. 六维乘法与几何分母

系数环是 QQ[u,Q,ell,lambda] 按已付权因子局部化。先在其首一商

$$
\mathcal A=A_0[T]/(F_6/(4\ell^2d))
$$

中取六个基底 1,T,…,T5。每次乘法都进行完整多项式回乘：

$$
\text{raw}=\text{quotient}\cdot\widehat F_6+\text{remainder},
\qquad \deg_T(\text{remainder})\le5.
$$

本次使用的分数始终存为

$$
a/(D^iE^j),\qquad a\in\mathcal A.
$$

D、E 的幂分别登记；相等检查通过显式交叉相乘和上述首一余式进行。没有把任意非零六维元素当作可逆元素，也没有把代数范数非零当作原点条件。参数分母逐一只剥此前已付权因子。

应区分两个陈述：首一商 A 是自由六维；在另外要求原点 D、E 非零后，本文得到的是同一点的有理恢复和方程等价。没有宣称整个局部化后的原解商仍是 A0 自由六维，也没有从这个表示推出图为空。

## 3. 同一个原 Gram 与两谱返回

选 rho 满足 rho²=d。因为 d≠0，两谱 p=1+rho、q=1−rho 互异。令

$$
b=\ell/2+m/(2\rho),\quad c=\ell/2-m/(2\rho),\quad a=1-\ell.
$$

以

$$
W_1=T_0/2+2uf,\quad
W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt
$$

恢复

$$
X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)}.
$$

所用 bp(q−p)、cq(q−p) 的逆只由已付 bc、Q、d 支付。设

$$
r=X-ap-ct,\quad s_G=Y-aq-bt,\quad
A_G=2f-2bX-2cY+2bc\,t.
$$

原四行 Gram 是

$$
(0,0,p,q),\quad(0,A_G,r,s_G),\quad
(p,r,0,t),\quad(q,s_G,t,0).
$$

原局部代数乘法与 tau、DK、原均值、N4、P2 均使用原定义，没有另换模型。两个原值恢复为

$$
h=1+v_0+\rho v_1,\qquad k=1+v_0-\rho v_1,\qquad
V=(1,w,h,k).
$$

本次实际返回了 tau(V)=lambda、二/三矩、D=bc(h−k)²、原 E0/N0/P1 及原一阶极化身份。原 N4(V) 采用已经证明的准确差身份

$$
QN_4(V)/2=N_Ff+N_Tt+N_C-QfH_A/u^2.
$$

当前同源矩 HA=0 和完整第二线均已实际为零，故原 N4(V)=0；这一步保留了修正项，没有再次设置完整通用展开门。

在 rho 扩张中写每条 singleton 方程为偶、奇两部分。因 rho≠0，两条谱方程同时为零当且仅当其偶、奇两部分均零。源实际重建了第二谱，并核验其等于第一谱的共轭。因此下面四条个别 N/P 方程没有用加权和代替另一谱。

## 4. 八条原方程的实际返回

分别返回 E1、EB_even、EB_odd、N1，以及

$$
N_B=N_4(G_B)-2\lambda P_{02}h^2,\qquad
P_B=P_2(G_B)-P_{02}h^3
$$

的偶、奇部分；C 谱取同一 rho 共轭。清分母后只删除已付权因子，不删除未付 T 首项。下表为删除已付因子后的多项式实际大小。

| 原方程 | D/E 幂 | 次数界 (u,Q,ell,lambda,T) | 项数 |
|---|---|---|---:|
| E1 | (0,2) | (16,9,13,14,5) | 41461 |
| EB_even | (0,2) | (17,10,14,14,5) | 50021 |
| EB_odd | (0,2) | (17,9,14,14,5) | 46082 |
| N1 | (0,2) | (17,10,14,14,5) | 43663 |
| NB_even | (2,3) | (26,16,21,25,5) | 339440 |
| NB_odd | (2,3) | (27,15,21,25,5) | 320588 |
| PB_even | (3,3) | (28,17,22,27,5) | 443050 |
| PB_odd | (3,3) | (27,16,22,27,5) | 421269 |

前四条仅剥一次 ell−u，后四条仅剥两次 ell−u；其它规范化仅除非零有理常数。每条的精确 SHA、原分母次数和删除记录保存在小回执。

原点 D、E 及各权分母非零，所以清分母和删除已付因子都双向保零。反向给定原参数及 F6=0、八式为零，再保上述原单位和原模型其余非零条件，原恢复式构造出同一 Gram、两个值以及本节列出的全部原矩、均值、N1、个别 N/P 方程。此为当前原值系统的完整返回，不是参数投影后的充分性猜测。

固定 (u,Q,ell,lambda) 后，T 的候选至多六个，再逐一检查原点单位与八式。参数本身仍未消去，不能由此声称参数图有限或排空。特别是表中大项数表明直接对八式继续大规模展开不是已付的小消元。

## 5. 再生源和实际凭据

源：

- notes/2026-11-27-unit211-general-Delta-nonzero-monic-six-actual-value-return-8542.py
- blob b8b86aaece6728374e91b018afa4cf98f8094440
- SHA256 6a0362da13dc06d05e83e1d33f03942dcab442b40a32a8e0bb7430b96330766f

依赖均由同一提交读取并在源内核对 SHA：

- 首一六维 helper：SHA256 5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6。
- 分列几何幂 helper：SHA256 8fef06d13684d0a6ab9a463c38287cabc2793c9f92cd43dd43544a7c8f7d3408。

实际 run45985977120/job140461591893；Python3.12.14、python-flint0.9.0、单线程；内层180秒/4GiB。

- 源72.157089702秒，驱动72.253398819秒，内层exit0，峰值460740KiB。
- 3613次六维乘法、3627次余式返回、23248个完整身份系数、9627次外部系数核验、15个已付参数逆。
- 完整八条均返回；没有新增未付逆或有限代数范数逆。
- stdout9174字节，SHA256 b93e0cc8c8057551b0f65649a98e855664f7a569e5e38e80e4e4e47948d1d7ca。
- 真正pull于2026-11-27 10:54:21.046240 UTC，前后提交e4f22fb07d4f0c4ef5606fc82961976c2d4f9251；根/topic README均无变。
- 小回执：notes/2026-11-27-unit211-general-delta-monic-six-full-values-receipt-8542.json。

只保存再生源、参数、SHA和小回执，不保存可再生大多项式缓存。当前一般图、E=0/W、Phi=0、R150及普通ISP均未完成；下一输入应利用原两点值/权重的直接恢复或更小原行，而不把这批大多项式改名重开旧投影门。
