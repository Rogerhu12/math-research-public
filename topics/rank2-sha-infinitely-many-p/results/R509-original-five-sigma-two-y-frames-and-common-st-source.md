# R509 — 同一五 sigma 的两个纯 Y 框架、全残余核与原 S/T 共同四输入

日期：2026-11-14。**状态：已证明。** 本篇把 R504 的新 degree65
方向接回 R493、R497、R500 的同一组五个原 sigma 输入，构造两个
完整纯 $Y$ 框架。全部五个输入和两个剩余伴随同时保留；
不是把两个分别压缩的边际事后拼成联合。

两个 odd 轴的真实符号相同，都是 R500 的 $\chi_V$；
两个 even 轴的绝对核心均为 $\beta=-\lambda$。
完整剩余两个伴随有共同核心 $\lambda^2$，可以合法压缩到
三个五 sigma 输出和一个独立 sigma。同一四输入还同时具有
原合格 $S_{34}$ 与 $T_{72}$ 两条显示的完整边际。

所有非轴条件仍按显示矩阵运输。本文不把边际身份提升为任意
条件中央零，主目标未完成。

## 1. 全部原输入及新 degree65 来源

令
$$
\delta^2=-3,\quad\omega=(-1+\delta)/2,\quad
\gamma=3+\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2.
\tag{1}
$$
五个输入按
$$
\boldsymbol u=(\xi_1,\xi_2,\xi_3,c,d_0)
$$
排列，余下独立输入为 $x=\xi_4$。原来源始终是
$-\nu_\sigma^{\otimes6}/84$，包含全部原周期和常数。

R500 的 $Z,V$ 行为
$$
z=(\delta,2\delta,\gamma,1,2),
$$
$$
v=((63+17\delta)/2,\,9-10\delta,\,-17+14\delta,\,
22+12\delta,\,17-3\delta),
\tag{2}
$$
度数 $27,3699$，彼此正交。
第一算术输出及其纯伴随继续是
$$
Y=Z+\bar\gamma x,\qquad T_c=\gamma Z-27x.
\tag{3}
$$
已有 $Z$ core $\beta$ 和 $V$ core $\chi_V\lambda$，
其中 $\chi_V^2=1$。

R504 的实际新方向经 R493 的 $\mathcal T$ 拉回，给同一五输入行
$$
\boxed{
r=(3+\omega,\ 2\delta,\ 6+3\omega,\ -1+\omega,\ 4),\qquad
R=r\boldsymbol u.
}
\tag{4}
$$
原全部来源的 $R$ core 为 $\chi_{65}\lambda$，
$\chi_{65}^2=1$。这里 $\chi_{65}$ 不与 $\chi_V$ 混同；
它沿原 $\pi_0\equiv2\bmod5,13$ 的真实 odd65 两 sigma 锚支付。

取 Hermitian 约定 $\langle a,b\rangle=\sum a_i\bar b_i$。
准确有
$$
N(r)=65,\qquad \langle r,z\rangle=33-\omega=(67-\delta)/2.
\tag{5}
$$
于是定义真正纯 $Y$ 轴
$$
\boxed{
J=\frac{27R-(33-\omega)Z}{2}.
}
\tag{6}
$$
它不含 $x$，正交于 $Z$，从而同时正交于 $Y,T_c$。
其原五输入系数全部在 $\mathcal O_K$：
$$
j=(23-20\omega,\,-8-13\omega,\,31+25\omega,\,
   -30+14\omega,\,21+\omega).
\tag{7}
$$
直接计算给
$$
N(j)=4266=54\cdot79.
\tag{8}
$$

## 2. 两个完整正交的纯 Y 框架

置
$$
\theta=18-35\omega=(71-35\delta)/2,\qquad N(\theta)=2179.
$$
原内积为
$$
\langle j,v\rangle=27\theta.
\tag{9}
$$
因此第二个 odd 纯 $Y$ 轴取为
$$
\boxed{
H=\frac{137J-\theta V}{27}.
}
\tag{10}
$$
其完整五输入系数是
$$
h=(68-83\omega,\,-14-28\omega,\,123+68\omega,\,
  -206+68\omega,\,105+35\omega).
\tag{11}
$$
全部为 CM 整数，并且
$$
\boxed{
\operatorname{Gram}(Z,V,H)=
\operatorname{diag}(27,3699,98777),\qquad
98777=7\cdot103\cdot137.
}
\tag{12}
$$

另置
$$
\boxed{
K=\frac{721V-\bar\theta H}{137}
 =\frac{158V-\bar\theta J}{27}.
}
\tag{13}
$$
其原系数同样完整给出：
$$
k=(163+83\omega,\,-7-98\omega,\,-46+107\omega,\,
 276+170\omega,\,42-63\omega).
\tag{14}
$$
则
$$
\boxed{\operatorname{Gram}(Z,J,K)=
\operatorname{diag}(27,4266,113918),\quad
113918=2\cdot7\cdot79\cdot103.}
\tag{15}
$$

两个纯伴随框架的准确矩阵是
$$
\boxed{
\begin{pmatrix}J\\K\end{pmatrix}
=
C\begin{pmatrix}V\\H\end{pmatrix},\qquad
C=\frac1{137}\begin{pmatrix}\theta&27\\721&-\bar\theta\end{pmatrix},
\quad \det C=-158/137.
}
\tag{16}
$$
特别在当前普通好素数处，
$$
(V,H)\in(p^n)^2\quad\Longleftrightarrow\quad
(J,K)\in(p^n)^2.
\tag{17}
$$
不同深度必须保为
$$
\theta V+27H\in137p^a,\qquad
721V-\bar\theta H\in137p^b,
\tag{18}
$$
而不是擅自变成 $V\in p^a,H\in p^b$。

## 3. 原五输入的整个可逆框架

保留剩余两个实际输入，定义
$$
\begin{aligned}
Q_1={}&(-3-9\delta)\xi_1/14+\xi_2
 +(9-\delta)c/14+(9+13\delta)d_0/14,\\
Q_2={}&(11+5\delta)\xi_1/14+\xi_3
 +(1+3\delta)c/7+(-13+3\delta)d_0/7.
\end{aligned}
\tag{19}
$$
则从原 $\boldsymbol u$ 到 $(Z,V,H,Q_1,Q_2)$ 的整个 $5\times5$
矩阵 $\mathcal M$ 满足
$$
\boxed{
\det\mathcal M=-380997=-27\cdot103\cdot137,
}
\tag{20}
$$
$$
\boxed{
\mathcal M\bar{\mathcal M}^{\,t}
=
\operatorname{diag}\!\left(
27,3699,98777,\
\frac17\begin{pmatrix}40&-6-19\delta\\-6+19\delta&46\end{pmatrix}
\right).
}
\tag{21}
$$
(21) 中前面三个轴与后两个轴的全部交叉项均为零。
最后一块内部不对角，其行列式为 $103/7$。

附证书给 $\mathcal M$ 及其整个逆；所有分母素数仅为
$2,3,7,103,137$。所以原五个独立输入同时深，与全部五个显示
输出同时深，是同一个真实事件。特别可以保每个原输入测试，
无须先作边际压缩。

## 4. 固定 ray、全部中心与两个相同 odd 符号

在 R500 和 R504 已有固定 ray 上增加
$$
\boxed{\pi_0\equiv1\pmod{79},\qquad \pi_0\equiv1\pmod{103}.}
\tag{22}
$$
这两个新模数与已有模数互素，且取的是单位类，故是兼容固定 CRT
细分，仍有无穷多个不同普通有理素数。原 ray 已有
$\pi_0\equiv2\bmod7$、$\pi_0\equiv1\bmod27$、
$\pi_0\equiv1\bmod137$，以及 $g_\pi=\pi_0/\bar\pi_0\equiv3\bmod4$。

令
$$
M_o=27\cdot7\cdot79\cdot103\cdot137=210691341.
$$
这些完整同余给一个方便的统一中心代表
$$
\boxed{g_\pi\equiv421382683=1+2M_o\pmod{4M_o}.}
\tag{23}
$$
因此
$$
g_\pi\equiv1\pmod{2N}
\quad(N=3699,98777,2666979),
\tag{24}
$$
而
$$
g_\pi\equiv1+N\pmod{2N}
\quad(N=4266,113918).
\tag{25}
$$
这里保的是 $2N$ 的完整中心，不只模 $N$ 的线性作用。

$V,H$ 的原五个系数模二各有三个单位，故是相同的标准 odd
半特征。由完整 odd 交织，(24) 给
$\mathcal K_{98777,p}=\chi_H I$，但还需确定实际标量。

置
$$
\gamma_{103}=11+2\omega,\quad N(\gamma_{103})=103.
$$
两个非零拉回
$$
[\gamma\gamma_{103}]^*\mathcal S_{3699}^{\rm odd},
\qquad
[3\delta]^*\mathcal S_{98777}^{\rm odd}
$$
都进入同一个标准 odd 空间
$\mathcal S_{2666979}^{\rm odd}$，因为
$$
3699\cdot721=98777\cdot27=2666979.
\tag{26}
$$
两个 CM 乘子的范数都为奇数，所以保持唯一 odd 半特征。
它们在当前普通处为单位，固定拉回与实际 $p$-core 逐项交换。
共同空间由 (24) 有一个 whole scalar core。对两个非零拉回
分别比较，得到绝对身份
$$
\boxed{\chi_H=\chi_V.}
\tag{27}
$$
因此没有增加一个未关联的 odd 符号；也没有从中央导数定标。

## 5. 两个 even 轴的 whole 绝对核心均为 −I

(7)、(14) 的原系数模二各有四个单位，故 $J,K$ 都是标准 even
线丛。(25) 在整个 canonical Heisenberg 群上给恒等交织：
$1+N$ 同时乘两个指标，新增中心因子为
$\exp(\pi i(2+N)ab)=1$，因为 $N$ 为偶数。
所以两个 whole 核各是一个 scalar，还需真来源锚。

取
$$
\gamma_{79}=10+3\omega,\qquad N(\gamma_{79})=79.
$$
R302 的原 degree2 参考 $\Theta$ 具有实际 core $\beta=-\lambda$。
以下两个非零固定拉回给完整锚：
$$
\Theta(3\delta\gamma_{79}s)\in\mathcal S_{4266},\qquad
\Theta(\gamma\gamma_{79}\gamma_{103}s)\in\mathcal S_{113918},
$$
因为
$$
N(3\delta\gamma_{79})=2133,\qquad
N(\gamma\gamma_{79}\gamma_{103})=56959.
\tag{28}
$$
二者在普通处均为单位 CM 拉回，其实际 core 仍为 $\beta$。
故在整个原 theta 空间而非仅某条 principal 线上，
$$
\boxed{
\mathcal K_{4266,p}=\mathcal K_{113918,p}=-I.
}
\tag{29}
$$
以上锚的实际乘子还可写成
$(-27+51\delta)/2$ 和 $166+99\delta$，附证书精确核其范数。

## 6. 同一原五输入上的全部联立核心

在完整框架 (19) 中，(27)–(29) 对整个来源逐点作用，保其他全部
生成变量。各原整行与剩余 $Q_i$ 的交叉项由 (21) 全消，所以
没有依赖隐藏生成变量的额外 flat twist。实际单轴核心为
$$
\boxed{
Z:\beta,\quad V:\chi_V\lambda,\quad H:\chi_V\lambda,
\qquad J:\beta,\quad K:\beta.
}
\tag{30}
$$
原 $R$ 的 $\chi_{65}\lambda$ 和原 $W'$ 的 $\beta$ 也在同一个
完整来源上继续成立。

原五 sigma 同时深的标量为 $\beta^5$。
(20) 将此域精确换成 $Z,V,H,Q_1,Q_2$ 同时深。
取消前三个正交单轴 core；其乘积为
$\beta(\chi_V\lambda)^2=-\lambda^3$。
因此剩余两个伴随的准确共同核心为
$$
\boxed{
\mu|_{(Q_1,Q_2)\in(p\mathcal O_p)^2}
=\lambda^2[I_3,\kappa I_2]_*\mu,
}
\tag{31}
$$
其中 $\mu=-\nu_\sigma^{\otimes5}/84$ 采用整个 (19) 框架。
没有将 (31) 拆成两个尚未单独支付的 scalar cores。

于是对任意非负整数 $a,b,c,t$，
$$
\boxed{
\mu|_{\substack{Z\in p^a,V\in p^b,H\in p^c\\
                         (Q_1,Q_2)\in(p^t)^2}}
=
\beta^a\chi_V^{b+c}\lambda^{b+c+2t}
 [\kappa^a,\kappa^b,\kappa^c,\kappa^tI_2]_*\mu.
}
\tag{32}
$$
在 $(Z,J,K,Q_1,Q_2)$ 中，对应式把
$\chi_V^{b+c}\lambda^{b+c}$ 换成 $\beta^{b+c}$，
并且仍保同一个原独立输入 $x$。

所有 $V,H,J,K,Q_i$ 都真正正交于 $Y,T_c$，故它们的完整核心与
第一 $Y$ 的 canonical CM trace、反射及角投影严格交换。
对 R497 的同一个 $h^\times$，准确有
$$
\boxed{
\int_{\substack{V\in p^b,H\in p^c,(Q_1,Q_2)\in(p^t)^2\\Y,T_c\ {\rm unit}}}
 \langle Y\rangle^{du}h^\times(T_c/\Omega)d\rho_0
=
\chi_V^{b+c}\lambda^{b+c+2t}J_S(u).
}
\tag{33}
$$
另一个框架给 $\beta^{b+c}\lambda^{2t}J_S(u)$。
(18) 是两式在不等深情况下实际应比较的条件，不能省略。

## 7. 合法四输入压缩及原同深非零支

(31) 允许在保留精确 $\lambda^{2t}$ 后约去两个共同伴随。
真正压缩来源为
$$
\boxed{
\mathcal L_3(s,t,u)=-\frac1{84}
 \prod_{\ell=1}^5\sigma(z_\ell s+v_\ell t+h_\ell u),
\qquad
\nu_3=\nu_{\mathcal L_3}\otimes\nu_\sigma(x).
}
\tag{34}
$$
它保 $(Z,V,H)$ 三个输出和独立 $x$，并非两个旧
$\mathcal L(Z,V)$、$\mathcal L(Z,J)$ 边际的拼接。
对只依赖这四个真实输入的任意连续测试或实际紧开域，
$$
\int_{(Q_1,Q_2)\in(p^t)^2}f\,d\rho_0
=\lambda^{2t}\int f\,d\nu_3.
\tag{35}
$$

原五个独立 sigma 同时深、$x$ 单位的真实事件现在是
$Z,V,H,Q_1,Q_2$ 同时深、$x$ 单位。
R497 的同一个非零值在压缩后准确为
$$
\boxed{
\int_{\substack{Z,V,H\in p^n\\x\ {\rm unit}}}
 d\log\langle Y\rangle h^\times(T_c/\Omega)d\nu_3
=\beta^{3n}A(\kappa^n),\qquad v_p=5n,
}
\tag{36}
$$
其中 $A$ 正是 R503 的固定解析函数。

同深纯伴随域 $V,H\in p^n$ 与 $J,K\in p^n$ 相同。
在这个完整域中，排除固定素数 $349,1123$ 后，
$$
\boxed{
Z\in p^n\quad\Longleftrightarrow\quad
W'\in p^n\quad\Longleftrightarrow\quad R\in p^n.
}
\tag{37}
$$
这里使用
$$
W'=\frac{(37+3\delta)Z+2V}{27},\qquad
R=\frac{(33-\omega)Z+2J}{27},
$$
以及 $N(37+3\delta)=4\cdot349$、
$N(33-\omega)=1123$。
所以旧 $W'$ 小管与新 $R$ 小管现在确为同一个原事件。
然而它们各自核心的拉回会移动不同的纯伴随条件；(37) 不将这些
拉回条件删除。

特别在 $\nu_3$ 中，
$$
\int_{\substack{V,H\in p^n\\Y,T_c\ {\rm unit}}}
 \langle Y\rangle^{du}h^\times(T_c/\Omega)d\nu_3
=\lambda^{2n}J_S(u).
\tag{38}
$$
余下的 $Z$ 单位边界仍为 $\lambda^{2n}B_0(u)$；
R503 的全部正浅环带公式继续适用。
新增的几何是同一来源的第二个混合方向 $R$ 和第二个纯伴随框架，
不是由多一条保持 $Y$ 的核心自动得到新的算术零。

## 8. 同一四输入中的原 S/T 两条全边际

这一步使用 R493 已付的完整 $\mathcal T^3=I$ 几何，
而不是只比较来源质量。记 $W$ 为原 R465 的 degree72 输出。
R493 给
$$
h_{\rm old}=\omega^2\mathcal T_*\rho_0,\qquad
(\mathcal T^2)_*\rho_0=-\omega^2(\rho_0+h_{\rm old}),
\qquad W_*h_{\rm old}=0.
\tag{39}
$$
将该篇的整个四乘四矩阵实际相乘，得到
$$
\boxed{
W_2=W\circ\mathcal T^2=R+(2+\delta)x
=R-\omega^2\bar\gamma x.
}
\tag{40}
$$
五个非 $x$ 系数恰是 (4)，自由系数 $2+\delta=3+2\omega$ 的
范数为七。附证书同时核
$$
C\circ\mathcal T=\omega^2x,\qquad
C=(\xi_1+\omega^2\xi_3-\omega\xi_4-c)/2,
\tag{41}
$$
与 R506 的完整自由输入运输一致。

原 $W$ 边际为 $6\delta T$，所以由 (39)，在同一个 (34) 中
准确有
$$
\boxed{
Y_*\nu_3=\nu_S,\qquad
(W_2)_*\nu_3=-6\delta\omega^2\nu_T.
}
\tag{42}
$$
两条固定 rank-two 来源同时保留在共同四输入里。
其 Gram 为 $34,72$，交叉项
$\langle Y,W_2\rangle=37-3\delta$。
(42) 是完整第一边际，不预先把含 $Z,V,H,x$ 的混合单位事件
变成 $S$ 或 $T$ 的条件中央。
这些条件仍须使用原完整 CM 行或后续真实 $W_2$ 核来运输。

## 9. 旧 W 与原四态也严格下降；T/U 的隐藏耦合保留

旧 R465 的 $W$ 不只是一条已经忘掉的输出。用整个
$\mathcal M^{-1}$ 相乘，得到
$$
\boxed{
W=\frac{10+\delta}{9}Z
 +\frac{40+28\delta}{1233}V
 +\frac{1-\delta}{137}H+\bar\gamma x.
}
\tag{43}
$$
$Q_1,Q_2$ 的两个系数严格为零。并且全部物理行满足
$$
\boxed{W+\omega^2W'+\omega W_2=0.}
\tag{44}
$$
因此 $Y,W,W'/2,W_2,R$ 全在同一个真实四输入空间中，
与两个 $Q_i$ 的全部交叉项为零。

令 $G=\operatorname{diag}(27,3699,98777,1)$，$a$ 为上述任一轴
在 $(Z,V,H,x)$ 中的显示行。其完整物理压深矩阵就是
$$
\boxed{
I_4+\frac{\kappa^n-1}{aG\bar a^{\,t}}G\bar a^{\,t}a.
}
\tag{45}
$$
在整个六输入框架中，它与 $I_2$ 构成块对角。
该轴的 canonical torsion 平移、完整 CM fiber 算子及 $p$-core
同样只作用于此四输入块；原各篇已付的全部绝对相位保持。
所以它们与 $Q_1,Q_2$ 的共同限制、缩放及真正推前逐项交换。

特别，设
$$
e_0=\rho_0,\quad e_1=\mathcal K_W\rho_0,\quad
h_{\rm old}=-\tfrac12\sum_{t\in E[2]}T_{t,W}\rho_0,
\qquad F=\mathcal K_{W'/2}^{\,2},
$$
$$
q=Fe_1,\qquad
u=e_0+h_{\rm old}/2,\quad v=e_1-h_{\rm old}/2,\quad
z=q-h_{\rm old}/2.
\tag{46}
$$
这是 R488、R496 的同一个原四态系统，保其原覆盖及所有规范。
由 (45)，构造这些来源的所有操作都与 (31) 交换。
因此每一态都具有同一个剩余 $Q$ 共同核心 $\lambda^2$，
并可准确推到 (34) 的四输入中。
原 $\mathcal K_W,F$ 的整个来源关系及四态矩阵在此推前后仍成立；
不是只保四条边际。

第一 $Y$ 和第一 $W$ 的完整 CM 投影也与此推前交换。
所以 R483、R499、R501 已付的 $S,T,S_{\rm new}$ 条件行及 $H_{\rm ref}$
参考行可保其余三个实际伴随，完整下降。
这里继续采用那些结论原本的第一 $[2]$ 覆盖、周期和测试规范，
不重新省略尺度或 tame 因子。参考伴随的总质量不因推前改变，
其未知导数和实际移动管仍必须保留。
这不宣称“四个剩余变量的 simultaneous CM character 自动为一”；
使用的是已经支付的第一轴完整投影与真正推前的交换。

也必须明确整个几何变换的不同情况。
$\mathcal T$ 和 R493 的反射 $\mathcal U$ 不保持这个四维物理块。
例如 (41) 的 $C$ 在全部新坐标中准确为
$$
\boxed{
\begin{aligned}
C={}&\left(-\frac1{18}-\frac{\delta}{27}\right)Z
 +\frac{-3+19\delta}{7398}V
 +\frac{127+24\delta}{98777}H
 +\frac{1-\delta}{4}x\\
&+\frac{-63+21\delta}{206}Q_1
 -\frac{16+15\delta}{103}Q_2 .
\end{aligned}}
\tag{47}
$$
两个隐藏系数都非零，故 $C$ 反射 $\mathcal U$ 不能直接作为
这个压缩四输入上的操作。完整矩阵中，$Z\circ\mathcal T$ 的
$Q_1,Q_2$ 系数分别为
$$
\frac{-63+42\delta}{103},\qquad
\frac{-125-59\delta}{206},
\tag{48}
$$
同样非零。附证书完整给
$\mathcal M_6\mathcal T\mathcal M_6^{-1}$、
$\mathcal M_6\mathcal U\mathcal M_6^{-1}$，保所有交叉块。
(39)–(42) 的证明是在原六输入先使用真实几何身份，再作推前，
所以不需要把 $\mathcal T$ 冒认为一个四输入变换。
后续若用 $\mathcal T/\mathcal U$ 运输具体域，仍须回到这些
完整六输入矩阵。

## 证书与依赖

- [全部五输入、两框架、中心锚与 T 几何的精确程序](../scripts/check-r509-original-five-sigma-two-y-frames.mjs)；
  [完整矩阵和数据](../scripts/check-r509-original-five-sigma-two-y-frames.json)。
  同一 BigInt 有理/CM 证书函数已在可用 V8 执行通过。
  包含整个 $\mathcal M,\mathcal M^{-1}$、完整六变量 $\mathcal T/\mathcal U$ 交叉块，以及旧 $W$ 的零隐藏系数；没有只给若干采样列。
- [R504：原 degree65 真来源及全部两轴核心](R504-original-two-axis65-core-and-complete-rectangles.md)。
- [R503：同一个测试的全部浅环带和固定 B0](R503-original-unit-annuli-and-single-shallow-boundary.md)。
- [R500：原 V3699、符号和完整输入规范](R500-original-pure-y-axis3699-and-complete-w-depth-complement.md)。
- [R497：原 S 的正纯伴随测试与非零同深网格](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
- [R493：保 Y 的原六 sigma 三阶几何](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
