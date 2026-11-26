# R150 附录：单位211非零均值的单位基点均值图之有限曲线覆盖与半权排除

日期：2026-11-26 UTC。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

**状态：以下完整有限纤维覆盖及整个半权分支排除已证明。** 共同规范p+q=2、u=bp+cq=1后，非零孤立点均值的原完整解只能落在下面明确构造的(l,Q)次数(18,10)曲线上；整个l=1/2已排除。高曲线的剩余原梯度及一般u仍开放。

本次数学断言全部执行通过，末尾报告序列化失败，实际exit1。第7节准确保留该区别，不把程序退出状态改写成成功。

## 1. 原范围与同一完整Gram

接续[原半比例和jet除数完整排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-isolated-mean-unit-base-mean-half-ratio-exclusion.md)，保原单位Frobenius代数及同一长度五物理支撑。
共同缩放取
$$
p=1-\kappa,\quad q=1+\kappa,\quad Q=1-\kappa^2,\quad
\ell=b+c,\quad a=1-\ell,
$$
$$
b=\frac{\ell q-1}{2\kappa},\quad c=\frac{1-\ell p}{2\kappa},\quad
D=\ell^2Q-2\ell+1,\quad bc=\frac{D}{4(Q-1)},\quad P_0=\frac{Q(\ell-1)}2.
$$
令 $\lambda=m/u_0=N_0/P_0$，$g=bc\,t$，$f$ 为原二次标量。
前稿已经排去 $\ell=0,\lambda=1/2$ 及 $g$ 的jet系数零面。本稿只在
$$
Q(Q-1)\ell(\ell-1)D\,\lambda(2\lambda-1)\Delta_g\ne0,
\quad
\Delta_g=2f+2Q\ell\lambda-Q\ell-2\lambda
\tag{1.1}
$$
上继续。$\lambda=0$ 另由[整个零均值分支](R150-appendix-essential-four-unit-two-plus-one-plus-one-nonzero-base-highest-zero-isolated-mean-exclusion.md)关闭。

原 $E_0=0,N_0=\lambda P_0$ 的全局图仍是
$$
V_2=2-\ell Q,\quad W_1=V_2/2-1+2f,\quad
W_2=V_2-2+f(V_2+2)-Qg+2\lambda P_0,
$$
$$
x=\frac{qW_1-W_2}{bp(q-p)},\quad
y=\frac{W_2-pW_1}{cq(q-p)},\quad t=g/(bc),
$$
$$
r=x-ap-ct,\quad s=y-aq-bt,\quad A=2f-2bx-2cy+2g,
\qquad
K_B=\begin{pmatrix}0&0&p&q\\0&A&r&s\\p&r&0&t\\q&s&t&0\end{pmatrix}.
\tag{1.2}
$$
沿前稿固定的原分子归一，六式依次为
$$
E_1,\ E_B+E_C,\ (E_B-E_C)/\kappa,\ 
3N_1-2\lambda P_1,\ \overline P-2\overline N,\
\overline N-2\lambda^3P_0.
\tag{1.3}
$$
记为 $M_0,M_1,M_2,M_3,M_4,M_5$，只删除已付非零因子。
$\overline P=aP_0+P_1+bP_B+cP_C$，$\overline N$同理；
原零点mean和最高式给 $\tau(U^2)=2m^2,\tau(U^3)=4m^3$，所以最后两式也是原必要式。

源码从原乘法、完整 $E,N,P$ 及一阶jet重建 (1.2)–(1.3)。
其中准确有
$$
\partial_gM_3=-Q\ell\Delta_g/2.
\tag{1.4}
$$
因此可全局解g，未引入未付的除数。

## 2. 缩放后的三条二次mean

令
$$
v=2\lambda-1,\qquad z=(2f-1)/v,\qquad
\lambda=(1+v)/2,\quad f=(1+vz)/2.
$$
此时 $\Delta_g=v(z+Q\ell-1)$，全部除数由
$$
\mathcal U=v(v+1)Q(Q-1)\ell(\ell-1)D(z+Q\ell-1)
\tag{2.1}
$$
支付。把 (1.4) 的唯一g解代入 $M_0,M_1,M_2,M_4,M_5$，
清分母、反复只移去与 $\mathcal U$ 的gcd、按词典首项首一化，
定义 $A_0,A_1,A_2,A_4,A_5\in\mathbb Q[v,z,\ell,Q]$。
其 $(v,z,\ell,Q)$ 次数为
$$
(2,4,4,3),\ (2,4,9,6),\ (2,4,8,5),\
(3,6,12,8),\ (3,6,12,9).
$$
前三式对 $(v^2,v,1)$ 的三行系数行列式，
仅移去 (2.1) 的因子后记为 $B(z,\ell,Q)$，次数 $(6,8,6)$。
每个原mean解满足 $B=0$。

## 3. 投影到(l,Q)的全部纤维有限

$B$ 的七个z系数的精确QQ lex基为
$$
\frac{(\ell-1)(7Q+80\ell^2-120\ell+40)}{80},\quad
\frac{Q(\ell-1)(2\ell-1)}2,\quad Q^2(\ell-1),\quad Q^2(Q-1).
\tag{3.1}
$$
末项在 (2.1) 上非零，所以每个合法(l,Q)上B都不是恒零z多项式，z纤维有限。

若三条mean的全部九个v系数同时零，其在z=1的理想包含 $Q^3\ell^2$，
所以先有z≠1。此时可从精确grevlex基中仅删已付单位和z−1因子；
所得lex理想包含
$$
\frac{-80Q^3\ell+68Q^2\ell+8Q\ell^2-Q\ell+21z-21}{21},
$$
$$
\frac{Q\ell(32Q^2-28Q+2\ell^2-3\ell+1)}2,\quad
Q^2\ell(4Q+\ell-5),\quad
\frac{Q^2\ell(4Q-3)^2}{16}.
\tag{3.2}
$$
Q、l非零依次迫 $(Q,\ell,z)=(3/4,2,-1/2)$，但该点D=0。
故至少一条mean始终为非恒零v多项式。每个z之上v纤维也有限。
两步支付整个投影的有限纤维条件，包含全部恒零系数例外。

## 4. 整个半权l=1/2排除

固定l=1/2仍保原五式。z=1处只移去已付单位，
前三条的QQ基包含
$$
v-Q/4,\qquad Q^2.
$$
所以该原纤维与Q≠0矛盾，不能在支付前删除。

z≠1时，将第一mean与其余四式分别作完整v结果式，
只移去已付单位及z−1因子；再将第一个与后三个作完整z结果式。
三个真正一元Q多项式次数为60、98、108，精确QQ gcd为
$$
\boxed{Q^{38}.}
\tag{4.1}
$$
只余禁止的Q=0，整个l=1/2为空。首项降次和孤立点没有被删掉。

## 5. 完整必要曲线覆盖

定义
$$
R_j=\operatorname{Strip}_{\mathcal U}\operatorname{Res}_v(A_0,A_j),\quad j=1,2,
\qquad
T_j=\operatorname{Strip}_{\mathcal U}\operatorname{Res}_z(B,R_j).
$$
每个原mean像点都满足 $T_1=T_2=0$。
由第4节，原完整解可继续限制在开集 $2\ell-1\ne0$。

这里不把平面gcd当作自动排除孤立公共点。
三条mean在四维仿射开集的每个非空不可约分量维数至少一；
第3节的有限纤维保证其像闭包同维。
像又落在两个非零投影多项式的公共零集上，故每个像闭包是一条公共曲线。
所以整个实际像，包括特殊点，都落在 $\gcd(T_1,T_2)$ 的零集中。
论证只用于三mean开集，没有对加入N/最高式后的有限零集误用维数下界。

定义完全确定的原QQ多项式
$$
\boxed{\mathcal C_{18}(\ell,Q)
=\operatorname{Strip}_{\mathcal U(2\ell-1)}\gcd(T_1,T_2).}
\tag{5.1}
$$
精确构造给 $(\deg_\ell,\deg_Q)\mathcal C_{18}=(18,10)$。
所有剩余原完整解必须满足它；本稿没有将这条必要曲线称作物理临界集。

## 6. 仍保原最高和N条件

$A_4=A_5=0$仍须满足。后继输入为关于 $(v^3,v^2,v,1)$ 的两组四行系数行列式：
$$
(vA_0,A_0,A_1,A_4),\qquad(vA_1,A_1,A_2,A_5).
$$
原解给非零核向量，故行列式必零。与B对z、再与C18对Q作真正结果式，
可保留全部有限交点。该新计算及一般u≠1仍在继续，不属于本稿的排空结论。

## 7. 实际执行、报告错误与源码修复

[自含源](../notes/2026-11-26-unit211-nonzero-mean-unit-base-scaled-projections-347c.py)
的实际执行版本固定于提交96819c8f4b69f55f513137692d3e4587f104196d，
SHA256为4d854f9f7a90ec14ee91d8e41e1fe9796b95cee5abae92b75d6de9431bba5351。

[run45795365604/job139824522922](https://github.com/Rogerhu12/math-research-public/actions/runs/45795365604/job/139824522922)
已实际通过三二次式和B的次数、(3.1)–(3.2)、半权(4.1)的全部数学断言，
随后完成两个mean投影、gcd及(5.1)的单位删除，
并通过最后的degrees(CC)==[0,0,18,10]断言。

第209行生成报告参数时，polyhash(CC)把FLINT整数指数交给JSON，
发生TypeError: Object of type fmpz is not JSON serializable。
因此真实exit1，驱动356.876653753秒、RSS323008KiB。
该错误发生在所有数学断言之后；不把程序状态改成exit0，
也不声称修复后的入口已经另一次完整成功运行。
修复只将指数显式转为Python int，数学源码未改。
后继高曲线源改用精确齐次多项式代入，继续尚未支付的交点，
不为打印摘要单独重算已闭门。

[实际小回执](../notes/2026-11-26-unit211-scaled-cover-execution-347c.json)
保exit1、失败位置、原stdout SHA及实际pull/规则身份。
全部数组从原源重建，不提交可再生大表。普通Hilbert ISP仍未完成。
