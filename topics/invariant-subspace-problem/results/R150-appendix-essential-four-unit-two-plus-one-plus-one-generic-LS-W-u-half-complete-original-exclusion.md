# R150：一般 W=0 图上整个 u=1/2 权线的原系统排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127。

## 1. 定理和范围

**定理。** 已登记的一般 LS、Delta=0、W=0 原物理图内不存在 u=1/2 的原 essential 2+1+1 解。因此该 W 图的余分支可支付 2u-1。

本证明处理整个权线，没有新增未付首项零面。它直接得到特征零原常数行 1；实际最终 Dpower=0，因此不需要用原 D 单位作最后的饱和排除。本定理没有把结论扩张到无 W 假设的一般 u=1/2 图，也不宣称一般 W 或普通 ISP 已完成。

沿用一般 W 原参数

$$
e=u-1,\quad Q=ek,\quad V=(e+1)k+2,\quad
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV}.
$$

在 u=1/2 上，精确化为

$$
e=-\frac12,\quad Q=-\frac k2,\quad
V=\frac{k+4}{2},\quad
\ell=\frac{k+1}{k},
$$

$$
bc=\frac{2k+3}{8k},\quad
P_{02}=\frac{k+2}{2},\quad \Phi=-1,\quad
H=-(k+2)(k+4).
\tag{1}
$$

整条线的系数分母和剥除内容只使用

$$
k,\quad k+1,\quad k+2,\quad k+4,\quad 2k+3.
\tag{2}
$$

k 来自 Q，k+2 来自 1-Q，k+4 来自原 W 坐标的 V，2k+3 来自原 bc。k+1 已由先前整个 k=-1 分支排除支付；也可由[整个 W/u=Q 排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-u-equals-Q-complete-original-exclusion.md)和本线 u-Q=(k+1)/2 支付。没有把任何仅数值非零的因子列入 (2)。

## 2. 完整原输入

源从原 Gram 重新生成全部必要式。为固定再生定义，令

$$
d=1-Q,\quad r^2=d,\quad p=1+r,\quad q=1-r,
$$

$$
b=\frac{\ell}{2}+\frac{u-\ell}{2d}r,\quad
c=\frac{\ell}{2}-\frac{u-\ell}{2d}r,\quad a=1-\ell,
$$

$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,
$$

$$
J=2u(1-u)+\ell Q,\quad
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q).
$$

在独立有限变量 x,y,t 中取 X=x+yr、Y=x-yr，

$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},
$$

$$
\lambda=\frac{V_2x+(2u-uQ-\ell Q)y-uT_0-(V_2+2u^2)f+bcQt}{P_{02}},
$$

$$
T=\frac{[\lambda P_{02}-(1-u)T_0]T_0-P_ff-\Phi bcQt}{QP_{02}}-\ell.
\tag{3}
$$

Gram 四行是

$$
g_0=(0,0,p,q),\quad g_1=(0,A_G,R_G,S_G),\quad
g_2=(p,R_G,0,t),\quad g_3=(q,S_G,t,0),
$$

$$
R_G=X-ap-ct,\quad S_G=Y-aq-bt,\quad
A_G=2f-2bX-2cY+2bct.
$$

原乘法为

$$
vz=(v_0z_0,\ v_0z_1+v_1z_0,\ v_2z_2,\ v_3z_3),
$$

单位为 (1,0,1,1)，tau(v)=a v0+v1+b v2+c v3。令 K(v)j=tau(gj v)、Dvec=K(1)、F2=tau(Dvec)=2f。三个 mean 为

$$
E_j=\epsilon_j-2K(Dvec)_j-2(Dvec^2)_j+2F_2Dvec_j,
$$

其中 epsilon1=2tau(g0g1)，其余 epsilonj=tau(gj²)。令

$$
\mathcal N(v)=2\tau(Dvec\,v^2)-F_2\tau(v^2)
-4\tau(v)\tau(Dvec\,v)+2F_2\tau(v)^2+\tau(vK(v)),
$$

$$
\mathcal P(v)=\tau((v-\tau(v){\bf1})^3),\qquad
P_j=3\tau((g_0-\tau(g_0){\bf1})^2(g_1-\tau(g_1){\bf1})).
$$

取 A2=2lambda²-2lambda+1、B3=4lambda³-6lambda²+3lambda-1，定义

$$
N_1=\mathcal N(g_0+g_1)-\mathcal N(g_0)-\mathcal N(g_1)
-\frac43\lambda P_j,
$$

$$
N_S=b\mathcal N(g_2)+c\mathcal N(g_3)
-2\lambda P_{02}(\ell+2T+A_2),
$$

$$
P_S=b\mathcal P(g_2)+c\mathcal P(g_3)
-P_{02}(\ell+3T+3A_2+B_3).
$$

固定原六式

$$
(E_1,E_{Be},E_{Bo},N_1,N_S,P_S)=0,
\tag{4}
$$

其中 E2=EBe+r EBo、E3=EBe-r EBo。前三 mean 和 N1 是二次式，后两式是三次式。所有 W 权身份、原 E0=0、N(g0)=2lambda P02、Pj=3(lambda-1-T)P02、P(g0)=P02 及 Gram 重建都实际乘回。加权 N/P 的必要性沿用此前同一原 HA/HB 迹，未换用不同原式或不同根。

## 3. 整条线的原六生成元：无新首项零面

[已登记全头 atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-H-nonzero-original-head-atlas.md)选择二次头列 (x²,xy,xt,t²)，其未付部分为 (k+2)J19。选择第 0、2 个原 cubic overlap 的三次头，未付部分为 C9。

在式 (1) 上，完整精确因式为

$$
J_{19}=-\frac14(k+2)^2(k+4)^3,
$$

$$
C_9=\frac12(k+1)(k+2)(k+4)^2.
\tag{5}
$$

式 (5) 分别独立用 BigInt 整数多项式和本次实际 Python 源乘回。所有因子都在 (2) 中，所以这里不依赖新近的整个 C9 排除，也没有把它的零纤维额外丢掉。

实际求出四条首一原二次规则，首项 x²、xy、xt、t²；再按总次数优先、x>t>y 的次序约化

$$
yq_0-xq_1,\quad tq_0-xq_2,\quad
tq_1-yq_2,\quad tq_2-xq_3.
$$

选第 0、2 行得到两条首一原三次规则，首项 y³、y²t。全部逆乘积、原六式组合及系数分母逐项返回。严格降单项式后得到六生成元

$$
\mathcal B=(1,x,y,t,y^2,yt).
\tag{6}
$$

三个变量各乘六个单项式的 18 条身份全部实际核为原六式组合，给出 Mx、My、Mt。任何原点的值列 v=(1,x,y,t,y²,yt)^T 满足 Mx v=xv 等式，且 v0=1。没有假设这些生成元在商中线性无关。

## 4. 原 24 行和完整十三次一元覆盖

从未用于首一三次规则的第 1、3 个 overlap、完整原 NS/PS、真乘法矩阵的同点交换子行，以及最初四条原必要行乘 x、y、t，得到固定 24 条六列原必要行。每个交换子在真实值列上为零，理由是 Mx v=xv 等已核原身份，而非宣称商模自由。

清分母和公共内容仅使用 (2)，每个缩放实际乘回。24 个多项式行的最大 k 次数依次是

$$
8,7,10,10,10,9,8,7,10,10,10,9,
13,11,12,12,10,11,15,13,14,15,13,14.
$$

五个非恒定列放在前面，做多项式无分式消元。五步主元次数是 6、13、21、29、36；每个精确除法实际乘回，不把中间主元零点从原图删除。

原行前五个索引固定为 (1,0,2,3,5)，第六行依次取

$$
4,\ 8,\ 10,\ 16,\ 13,\ 17.
$$

六个完整 cofactor 的全部五个非恒定列组合实际为零，常数列原多项式次数分别为 44、44、44、44、45、45。只剥 (2) 后各为 13 次，并且实际一元 Bézout 两乘回的共同覆盖为下列 primitive 多项式的非零常数倍：

$$
\begin{aligned}
F_{13}(k)={}&5120k^{13}+29056k^{12}+1448k^{11}
+2223520k^{10}\\
&+34723590k^9+219823272k^8+798383289k^7\\
&+1863202972k^6+2913699520k^5+3064262397k^4\\
&+2099984956k^3+860964576k^2+169255236k+5513568.
\end{aligned}
\tag{7}
$$

完整 QQ 因式乘回保留这一个 13 次因子，重数 1。因此任何原点的权参数必满足 F13(k)=0；此前没有给有限变量代入猜测值。

## 5. 整个十三维 QQ 商上的原常数 1

取整个

$$
A=\mathbb Q[k]/(F_{13}).
$$

所有系数及原单位在整个 A 上作精确计算，每个逆都由 QQ[k] 的 Bézout 两项乘回得到。代码不会把一个非单位硬当作逆；本次实际没有未处理的非单位分裂。

上述固定 24 条原必要行在 A 上的初始秩已经是 6。完整源仍加入六个原多项式的真乘法行并核闭包，共保存 48 条生成行，最终秩 6。它实际返回

$$
\sum_j\alpha_j(k)R_j=(1,0,0,0,0,0)
\quad\text{于整个 }A.
\tag{8}
$$

全部六列和每个有限逆都直接乘回，累计 200 次真逆核验。证书中的 DpowerReturned=0 正是常数 1；不需要额外使用 Dphysical 非零假设。由真实列 v0=1，式 (8) 矛盾。

这排除了 (7) 的全部复根、全部谱嵌入及整个商代数；没有模素数提升，也没有数值采样。结合完整一元覆盖，整条 u=1/2 原分支被排除。

## 6. 可用推论

余 W 图可支付 2u-1=2e+1。另结合已经完成的[一般 ell=0 排除](R150-appendix-unit211-general-ell-zero-complete-original-exclusion.md)和[一般等权排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，全头 atlas 的另一组列 (x²,xt,y²,yt) 的全部未付因子

$$
(k+2)(2e+1)\{2ek-(k+2)^2\}
$$

均可支付，因为

$$
\ell=-\frac{u\{2ek-(k+2)^2\}}{kV}.
$$

这只给新的四个原二次头在全余图可逆；这些四头未必兼容简单单项式下降次序。后续的 6×4 完整三次一致性输入仍需其自己的原身份和实际回执，本条不把它记成已执行的六生成元构建。

## 7. 自含源和真实 Actions 回执

源：

notes/2026-11-27-unit211-generic-LS-W-u-half-complete-original-return-8542.py

实际 source blob：282e95f68f77db2dd209bd93590465ef23acb7d0。

实际源码 SHA-256：

5d7064468698db3d580e0116e0814b15df1bef246428838f2294727838077582

唯一 GitHub Actions run 45961582428，job 140380414506，run attempt 1：

- 源内部总墙钟：0.617815147 秒，峰值 RSS 40,100 KiB。
- 驱动总墙钟：0.675933720 秒，最大 child RSS 40,828 KiB。
- 实际 source exit code：0。
- 原 13 维 QQ 返回墙钟：0.376858264 秒。
- stdout：9,207 字节，SHA-256 d9ece7e80ebacd4c57b9face83863d3bbf3c3a3ea66da5d677827d4d5e90c83f。
- 最终六列常数证书：108,591 字节，SHA-256 224ceb3e01680e8779b614b68aea66619f370fa398d2723be87dbef9dddc8452。证书可由完整源再生，不保存大系数缓存。
- 源内限制为 180 秒、4 GiB。本次没有超时、内存失败、跳过的大因子或未完成分支。

驱动于 2026-11-27 07:53:40.677368 UTC 真实 pull；前后提交均为 4ae67dc5b7144c6c9adf0b16a057a6ad13a06cd7。根 README 与课题 README 均无变化，对应 git blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d 和 5fbd905291dd044c88d35bd9c07ac0e586ff795a。

小回执保存完整驱动记录、每个 cofactor 的行索引与实际回乘摘要，以及最终整 QQ 返回。论文正文和小回执在 create_blob 后均 fetch_blob 全文回读核对。本条是新的整单参权线输入，没有重跑此前冻结的一般 W 二维大系数门。

