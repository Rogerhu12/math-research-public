# R686 — 原 W−bY Y 完整核心、同源失败支与新增纯 S 隐藏门

日期：2026-11-15。**状态：已证明。**

本文保持 R679 的同一个 $q_N^\sharp$，支付原 Y 正交方向
$Z=W-b_YY$ 的完整来源核心。它不是从范数猜出的 whole 标量：
实际核心把原来源送到 Y 反射，绝对系数由同一三轴联合确定。
原 carry 的全部方向以及真正 cd 返回权都与 Y、Z 同时正交，
所以这里原本可能出现的十三个 Z 次数实际只剩零次项。

由此将原 W/Y 两个不同 unit cut 的进入支、近相消支及其深补域，
准确送回原来源与原 W 核的第二态；没有添加新的来源中央零。
另一个直接算术结果是：R679 的 cd 端点纯 S 身份可提升为
**未附 Z 条件的真实 $E_{YW}$ 深门**的整条 S 来源，
并能保全部 Z 环带。这些都是同一个原测试的实际条件。

## 1. 两个完整正交框架

保原 $b=17,\omega^2+\omega+1=0,\delta=1+2\omega$，
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0}.
$$
原六输入按 $(\xi_1,\xi_2,\xi_3,x,c,d)$ 排列，且
$$
A=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,
\quad Y=A+c+2d,\quad W=A+3\delta c+4d.
$$
其范数分别为 $29,34,72$，原投影系数为
$b_Y=(20+3\omega)/17$。置
$$
\boxed{
Z=W-b_YY,\qquad
17Z=(-3-3\omega)A+(31+99\omega)c+(28-6\omega)d,
}
$$
$$
\boxed{E_{YW}=(5+6\omega)A-29c-(58+87\omega)d.}
\tag{1}
$$
三个行正交，准确为
$$
\boxed{
\operatorname{Gram}(Y,17Z,E_{YW})
=\operatorname{diag}(34,8942,7627),\qquad
\det\frac{(Y,17Z,E_{YW})}{(A,c,d)}=8942.
}
\tag{2}
$$
这里 $8942=2\cdot17\cdot263$，$7627=29\cdot263$。
当前 ray 已在 R515 加入 $\pi_0\equiv1\bmod263$；
所有 (2) 的非单位素数都在原固定坏集中。

还置
$$
a_W=17-3\omega,\qquad V=36Y-a_WW.
$$
同一原平面的另一完整正交框架是
$$
\boxed{
\operatorname{Gram}(W,V,E_{YW})
=\operatorname{diag}(72,18936,7627),\qquad
\det\frac{(W,V,E_{YW})}{(A,c,d)}=-18936,
}
\tag{3}
$$
其中 $18936=72\cdot263$。实际逆关系为
$$
\boxed{
36Y=V+a_WW,\qquad
612Z=263W-(20+3\omega)V.
}
\tag{4}
$$
这些框架保留原 A 的三个伙伴，未忘去任何原输入。
R515 已列同度8942的 Y 伴随；下面新增的是本原联合上的准确核、
原 carry 逐点不变以及实际失败支。

## 2. whole E7627 与原 Z 核的绝对来源身份

原 C 旋转逐个固定 A、Y、W、Z、$E_{YW}$。
它们在每个原分支上的模二非零系数个数
对 Y、17Z、$E_{YW}$ 分别为 $4,4,5$。
所以三个方向在同一完整
standard even34、even8942、odd7627 格中，没有删掉 flat 特征。

原 fixed ray 给
$$
g_\pi\equiv1\pmod{15254}.
$$
因此整个 odd7627 核是某个真实标量 $\chi_E$。
其绝对平方由以下非零原两 sigma 联合支付：
$$
\sigma(2s+33\gamma_7t)\sigma(33\bar\gamma_7s-2t),
\qquad \gamma_7=3+\omega.
$$
两个输出范数均为
$4+33^2\cdot7=7627$，交叉项为零；
每轴恰一奇、一偶系数，故保标准 odd 半特征。
同两个原 sigma 同时深的系数为 $\beta^2=\lambda^2$，
与两输出的 $\chi_E^2\lambda^2$ 比较，得到
$$
\boxed{\chi_E^2=1.}
\tag{5}
$$
这使用同一个完整联合，不从质量或中央值定号。

令 $\chi_A=\chi_{29,p}$ 为已付原 A whole 标量，$\chi_A^2=1$。
原全 $A,c,d$ 同深系数为 $\chi_A\lambda^3$。
由 (2)，这正是 $Y,Z,E_{YW}$ 同深的同一事件和同一物理缩放。

原 entire S34 的核是 $\lambda R_Y$，其中 $R_Y$ 只反射 Y，
保持 Z、$E_{YW}$ 及所有伙伴。将已付 $\chi_E\lambda$ 与
Y 核从这个完整三深身份消去，得到
$$
\boxed{
K_Z\mu_0=\gamma R_Y\mu_0,\qquad
\gamma=\chi_A\chi_E\in\{1,-1\}.
}
\tag{6}
$$
这里 $K_Z$ 按外部因子 $\lambda$ 归一。
(6) 是整个原六输入来源的身份，不只是其 Y 边际。

为明确规范，在完整 $2\cdot8942$ 中
$$
g_\pi\equiv9995\pmod{17884},\quad
9995\equiv3\pmod4,\quad
9995\equiv-1\pmod{17},\quad
9995\equiv1\pmod{263}.
\tag{7}
$$
本篇**没有**把这个 whole 交织认成 scalar；
(6) 是以原来源锚定的实际作用。反射与 Z 核按两个完整正交轴交换，
故同一 Y 反射态也由 (6) 返回原态。

## 3. 原所有 carry 方向实际上被 Y/Z 和 W/V 同时固定

原四输入行是
$$
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
D_*=D_4+\frac{5+6\omega}{29}A,\quad
H=F-C=D_4+c+(2+3\omega)d.
$$
直接代 (1) 有
$$
\boxed{H=D_*-\frac{E_{YW}}{29}.}
\tag{8}
$$
所以 H 与 Y、Z 均正交。
原 C、$H_1=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x$、
$D_*$ 均与 A 正交，故也与 Y、Z、W、V 正交。
于是
$$
E_{\rm test}=H+14C,\qquad
G=13H_1+(3-2\omega)(H+C)
\tag{9}
$$
及其原单位逆都同时保持。

因此原 $q_N^\sharp$ 的 C-unit、H-deep 门、六次/十二次多项式、
新增 $G^6$ 以及全部旧伙伴，在 Y/Z 或 W/V 任一轴缩放/反射下
逐点保持。旋转支用同一整数 $\mathsf J$ 运输这整个结论。

同样，R671 的 $j=N,M=0$ 真 cd 返回权
$$
q^{cd}_N=
1_{\{C^\perp\ {\rm unit}\}}\,
\mathcal P^\sharp
\left(H,\ 14C^\perp+\kappa^N K,\
G_\perp+(3-2\omega)\kappa^N K\right),
\qquad K=H-\frac{406}{143}D_*,
\tag{10}
$$
也逐点保持。$\mathcal P^\sharp$ 使用 R679 的混合物理规范，
不是将十二次项错误地除以六次周期。

特别 (10) 若按 Z 作次数不超过十二的展开，
**所有正次系数都准确为零**。
不能把它虚构成十三个独立来源或十三个新算术条件。
R669/R679 在 $t\ne1$ 的共同 E 门权则不具有这个不变性；
本篇不将 (10) 免费用于那些不同的返回权。

## 4. 两框架的完整实际矩形

设 $\phi$ 是任意有界连续的原共同伙伴权：
它只依赖同时正交于 Y、W 的四个伙伴。
上述 $q_N^\sharp,q_N^{cd}$ 及再附 $E_{YW}$ 深/浅门都属于此类。
令
$$
\rho_0=\phi\mu_0,\qquad
\rho_1=\phi K_{72,W}\mu_0 .
$$
所有下式均保原完整六输入，逆映射只在相应整像上使用。

由 (6)、Y 核及逐点不变性，对 $a,b\ge0$，
$$
\boxed{
\rho_0|_{\{Y\in p^a,\ Z\in p^b\}}
=\gamma^b\lambda^{a+b}
 (P_{Y,\kappa^a}P_{Z,\kappa^b})_*R_Y^{a+b}\rho_0.
}
\tag{11}
$$
其核心在整个 Y/Z 平面同时深时是 $\gamma\lambda^2$。

$K_{72,W}^2=I$ 已在原 whole S72 支付。
W/V 同深与 Y/Z 同深是同一平面事件，故
$$
K_V\mu_0=\gamma K_W\mu_0,\qquad
K_VK_W\mu_0=\gamma\mu_0 .
$$
这支付原 V 核在两态上的绝对号；没有重新猜一个范数标量。
于是
$$
\boxed{
\rho_i|_{\{W\in p^a,\ V\in p^b\}}
=\gamma^b\lambda^{a+b}
 (P_{W,\kappa^a}P_{V,\kappa^b})_*
 \rho_{\,i+a+b\ ({\rm mod}\ 2)},\qquad i=0,1.
}
\tag{12}
$$
(11) 没有被延伸为 $K_Z$ 在 $\rho_1$ 上的未经计算作用。
(12) 只使用真实 W/V 两态闭包。

## 5. 新 q♯ 的原 S 零可进入更大的真实隐藏门

现在取 $\phi=q_N^\sharp$，并仍固定 $N\in4\mathbf Z_{>0}$。
在 $n\ge N$ 时，原域准确满足
$$
\boxed{
\{Y\in p^n,\ c,d\in p^N\}
=\{Y\in p^n,\ Z\in p^N,\ E_{YW}\in p^N\}.
}
\tag{13}
$$
这是 (2) 的整可逆换元，不依赖一个边际近似。

在 $n=N$ 使用 (11)，因 N 是四倍数，其全部反射/未知符号幂为一。
R679 的完整 cd 端点是 $\lambda^{4N}\nu_S$；
从 (13) 去掉 Y/Z 两个已付核，得到整条测度身份
$$
\boxed{
Y_*\!\left(1_{\{E_{YW}\in p^N\}}q_N^\sharp\mu_0\right)
=\lambda^{2N}\nu_S.
}
\tag{14}
$$
这是未附 Z 条件的原隐藏域，不只是某个 principal 导数。

原完整 $\pi_4$ 返回还给 $Y_*(q_N^\sharp\mu_0)=\lambda^N\nu_S$。
所以 (11)、S 的偶性以及 (14) 支付以下整条第一来源表：

| 原完整条件 | Y 来源 |
|---|---|
| $E_{YW}\in p^N,\ Z\in p^m$ | $\lambda^{2N}(\gamma\lambda)^m S$ |
| $E_{YW}\notin p^N,\ Z\in p^m$ | $(\lambda^N-\lambda^{2N})(\gamma\lambda)^m S$ |
| $E_{YW}\in p^N,\ v_p(Z)=m$ | $\lambda^{2N}(\gamma\lambda)^m(1-\gamma\lambda)S$ |
| $E_{YW}\notin p^N,\ v_p(Z)=m$ | $(\lambda^N-\lambda^{2N})(\gamma\lambda)^m(1-\gamma\lambda)S$ |

这里 $m\ge0$，每行仍是同一个 $q_N^\sharp$。
$1-\gamma\lambda$ 是原 R410 已付的 $1-\lambda$ 或 $1+\lambda$，均为单位。
旋转支把 $Y,W,Z,E_{YW}$ 全部转置，另乘原 $\epsilon_i$。

因此原 $J'_S(0)=0$ 确实合法传到表中所有相应的完整 Y-unit 条件行。
表中没有把 W 的 moving unit/log 测试替换成 Y，也没有给相同条件下
的 T 行赋零。

## 6. 保完整 unit cut 的 Z 差方程

记
$$
f_w(x)=1_{\{x\ {\rm unit}\}}\langle x\rangle^{d_pw},\qquad
B(w)=\langle b_Y\rangle^{d_pw}.
$$
对第4节任意同一个权 $\phi$，定义
$$
S_\phi(w)=\int f_w(Y)\,d\rho_0,\qquad
T_\phi(t;w)=\int f_w(b_YY+tZ)\,d\rho_0.
$$
$t$ 是物理伸缩参数，不是 Mellin 变量。
因为 principal $f_w$ 是偶函数，(6) 给准确关系
$$
\boxed{
\int_{Z\ {\rm unit}} f_w(b_YY+tZ)\,d\rho_0
=T_\phi(t;w)-\gamma\lambda T_\phi(-\kappa t;w).
}
\tag{15}
$$
这对所有 $t\in\mathcal O$ 都保原实际单位 cut；
特别 $t$ 单位时仍保近相消域。

置
$$
H_\phi(t;w)=T_\phi(t;w)-B(w)S_\phi(w).
$$
纯 Y 的 Z-unit 行是 $(1-\gamma\lambda)S_\phi$，所以
$$
\boxed{
H_\phi(t;w)=
\int_{Z\ {\rm unit}}\{f_w(b_YY+tZ)-f_w(b_YY)\}\,d\rho_0
+\gamma\lambda H_\phi(-\kappa t;w).
}
\tag{16}
$$
若 $t\in p\mathcal O$，两个 cut 都恰为 Y-unit。
此时 $H_\phi$ 是一个真正收敛的原小参数观察，而不是零：
$$
\boxed{
\frac1{d_p}\partial_wH_\phi(-\kappa;0)
=-\sum_{r\ge1}\frac{\kappa^r}{r\,b_Y^r}
 \int_{Y\ {\rm unit}}Z^rY^{-r}\,d\rho_0 .
}
\tag{17}
$$
各真实矩整，所有 $1/r$ 分母保留。第 R 项后的尾至少在
$p^{R+1-\lfloor\log_p(R+1)\rfloor}\mathcal O$；
没有将这些未知负矩另赋零。

对 (10)，原 R671 的 $A_T$ 恰为
$T_{q^{cd}_N}(\kappa^N;w)$，且
$S_{q^{cd}_N}=J_S$。
因此 (15)–(17) 是同一个原固定 cd 行的真实差方程，
不是增加一组没有算术来源的 Z 权。

## 7. 两个失败支完整返回原来源及原 W 第二态

现在取 $t=1$。在同一原六输入上置
$$
\mathcal G=\{Y,Z,W\ {\rm unit}\}.
$$
定义实际三单位相对行
$$
G_\phi(w)=\int_{\mathcal G}
 \{f_w(W)-f_w(b_YY)\}\,d\rho_0.
$$
(16) 中剩余两支恰为
$$
\mathcal D_+=\{Y\in p,\ Z\ {\rm unit}\},\qquad
\mathcal D_-=\{Y,Z\ {\rm unit},\ W\in p\}.
\tag{18}
$$
在 $\mathcal D_+$ 上 W 自动为单位。
在 $\mathcal D_-$ 上，由 (4)，Y/Z-unit 准确等价于 V-unit。

定义两个完整来源函数
$$
Z_\phi(\kappa;w)=\int f_w(Z-\kappa b_YY)\,d\rho_0,
$$
$$
V_\phi(\kappa;w)=
 \int f_w\!\left(\frac{b_Y}{36}(V+a_W\kappa W)\right)\,d\rho_1 .
\tag{19}
$$
第一式的 unit cut 自动就是 Z-unit；
第二式的 unit cut 自动就是 V-unit。
它们不是把一个非单位值放入 principal log。

原 Y 核和 (12) 分别给
$$
\boxed{
\int_{\mathcal D_+}f_w(W)\,d\rho_0
=\lambda Z_\phi(\kappa;w),\qquad
\int_{\mathcal D_-}f_w(b_YY)\,d\rho_0
=\lambda V_\phi(\kappa;w).
}
\tag{20}
$$
第一条用 $R_Y$ 把 Y 送到 $-\kappa Y$；
第二条必须使用原 $\rho_1$，其观察为 (4) 的
$b_Y(V+a_W\kappa W)/36$。
这两个真实来源号不能合并。

将 (18)–(20) 代 (16)，得到原整个失败支的同源关系
$$
\boxed{
H_\phi(1;w)=
G_\phi(w)+\lambda Z_\phi(\kappa;w)
-\lambda V_\phi(\kappa;w)
+\gamma\lambda H_\phi(-\kappa;w).
}
\tag{21}
$$
所有 moving unit cut、原 carry 门、额外隐藏条件及其余伙伴均保留。
这不是以两个边际重新拼接一个联合。

## 8. 同 q♯ 的真实算术代入与质量

对未附额外门的 $\phi=q_N^\sharp$，
完整 $\pi_4$ 返回及 R679 的原 S/T 规范给
$$
\boxed{
\lambda^N\{6\delta J_T(w)-B(w)J_S(w)\}
=G_\phi(w)+\lambda Z_\phi(\kappa;w)
-\lambda V_\phi(\kappa;w)
+\gamma\lambda H_\phi(-\kappa;w).
}
\tag{22}
$$
这里 $\beta^N=\lambda^N$。
原 W 核只改变 W 轴，且 $\pi_4$ 的线性行空间在这次变换下保持，
$\phi$ 又逐点不变，所以原 $\pi_4$ 中性亦准确传至 $\rho_1$。
可直接把中性式限制 W-deep 后，用其整像逆证明这一点。

因此这一未附额外门的 $\rho_0,\rho_1$ 的完整质量都为零：
原 W 边际是 $6\delta T$，且原 $K_{72}T=T$。
(22) 右边四个显示行的质量于是分别为零。
所有尺度 log 项是在完整来源和质量等式后处理，没有预删。

为说明额外隐藏门的区别，对一般第4节权设
$$
m_0=\rho_0(1),\qquad m_1=\rho_1(1).
$$
准确有
$$
S_\phi(0)=(1-\lambda)m_0,\quad
T_\phi(1;0)=m_0-\lambda m_1,
$$
$$
Z_\phi(\kappa;0)=(1-\gamma\lambda)m_0,\qquad
V_\phi(\kappa;0)=m_1-\gamma\lambda m_0.
\tag{23}
$$
所以 (21) 的总质量两边均为 $\lambda(m_0-m_1)$。

对 $\phi=q_N^\sharp1_{\{E_{YW}\in p^N\}}$，
(14) 给 $m_0=0$，**没有**给 $m_1=0$。
对 $\phi=q_N^{cd}$ 亦不能从第一 S 来源推出其 W 第二态质量零。
因此局部 (19) 中的 $b_Y/36$ 尺度 log 必须完整保留。
(14) 的真实纯 S 隐藏门不授权删除这些局部 T 补偿。

若仅假设两个原中央导数为零，(22) 的准确后果是其右边的
完整中央导数组合为零。
没有得到 $G_\phi$、$Z_\phi$、$V_\phi$ 或 (17) 单独为零。
R679/R685 的已知非零角域仍须逐项放进这些原完整函数；
本文没有把一个真子域的非零冒作 (22) 的全行非零。

新增实质是 (6)、(11)、(12) 的完整原两框架，
(14) 的较大真实 S 条件域，以及 (20)–(22) 对两个原失败支的
准确来源返回。原主目标仍未完成，剩余为这个同源式中
实际三单位相对项与两原完整来源的算术比较。

## 9. 可复现证明证书；不保存可重算数据

按根 README 第15条，只提交以下独立脚本，不提交可重算 JSON：
[check-r686-original-yz-core-and-st-unit-carries.js](../scripts/check-r686-original-yz-core-and-st-unit-carries.js)。

运行参数：无额外输入文件、无网络、无第三方依赖。
$$
\texttt{node scripts/check-r686-original-yz-core-and-st-unit-carries.js}
$$
脚本向标准输出生成临时证书，并向标准错误打印 SHA256。
完整核心已在本会话 V8 运行，run 标记
`R686-v8-20261115T050848Z`，共54条准确检查；
全部为 $\mathbf Z[\omega]$ 的 BigInt 运算。
标准输出 UTF-8 字节的 SHA256 是
$$
\texttt{374028b50dd5239d321e6110853fe708eacd493bcbca61fdc81590aa559f9f3d}.
$$
它核全部原六维行、两个 Gram/行列式、完整门恒等、
四轴逐点不变、半特征、原 CRT 和非零两 sigma 锚。
普通核心、全量词、真实测度及单位分区的证明在正文，未由抽样替代。

公开 Actions [run 43680615234](https://github.com/Rogerhu12/math-research-public/actions/runs/43680615234)
已在提交 `e17cb0d47dad8914d866d38e1c0d53f48dfae35e` 按上式、无额外参数执行成功，
54条准确检查全部通过，stdout 的 SHA256 与上列值完全相同；未保存可重算输出。
上述 V8 标签只记先前真实环境，不冒充公开 run_id；附带检查不作为正文发布门。

主要依赖：
[R443](R443-original-residual-quarter-source-and-complete-central-return.md)；
[R515](R515-original-two-dimensional-st-source-and-same-source-sigma-carry.md)；
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)；
[R671](R671-fixed-depth-cd-return-and-original-exterior-filters.md)；
[R679](R679-neutral-degree-twelve-three-s-and-exterior-return.md)。
