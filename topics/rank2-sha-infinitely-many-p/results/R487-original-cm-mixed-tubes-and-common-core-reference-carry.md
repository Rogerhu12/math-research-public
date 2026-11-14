# R487 — 原伴随 CM 混管、同一两态核心与参考来源的非齐次 carry

日期：2026-11-14。**状态：已证明。** 本篇把 R483 的原五伴随
CM 投影完全展开，分清实际平移来源和外部单位尺度。去掉后者、
但保留全部平移支及权重，得到同一个原六输入中的固定来源和。
在一条兼容的固定无限 ray 上，它们仍保 R465 的原两态 $W$
核心。参考来源的两个 $W$ 单位质量和一个不含未知参考导数的
非齐次 carry 因而可以在这个共同核心中准确写出。

原 CM 投影与上述来源和的混管差没有删除：本文给它的完整
逐支公式，并将不同管的交叠严格局限到同一等赋值区域。
这仍未把所有 carry 送入三条实际秩二曲线的已知中央零，主目标
未完成。

## 1. 同一原来源、物理坐标与核心

沿用 R465、R483 的 $b=17$、$\delta^2=-3$、
$\omega=(-1+\delta)/2$、同一物理周期及原六输入。记
$$
\gamma_{13}=4+\omega,\qquad\gamma_{19}=5+2\omega,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1.
\tag{1}
$$
两套物理输出为
$$
(W,\mathbf Q)=(W,Q,U_t,R_1,R_2,R_3),\qquad
(Y,\mathbf Z)=(2Y_s,2Q_s,2U_s,R_1,R_2,R_3),
$$
对应标准 theta 次数分别是
$$
\mathbf N_M=(72,1624,252,60,2310,4466),\qquad
\mathbf N_L=(136,3480,1020,60,2310,4466).
\tag{2}
$$
R465 的同一两态写为 $\mathcal F_i^M,\mathcal F_i^L$，$i=0,1$。
它们满足整个来源身份
$$
K_{72,W}\mathcal F_0^M=\mathcal F_1^M,\qquad
K_{72,W}\mathcal F_1^M=\mathcal F_0^M.
\tag{3}
$$

R484 的实际坐标变换为 $C_6=\operatorname{diag}(C,I_3)$，
其中
$$
C=\begin{pmatrix}
(37+3\delta)/68&(1-3\delta)/60&(-31+3\delta)/510\\
(29+87\delta)/68&(-29+3\delta)/60&(29+87\delta)/510\\
(1+3\delta)/68&(1-3\delta)/60&(239+3\delta)/510
\end{pmatrix}.
\tag{4}
$$
特别
$$
W=cY+r(\mathbf Z),\qquad c=\frac{37+3\delta}{68},\qquad
r(\mathbf Z)=\frac{1-3\delta}{60}Z+
             \frac{-31+3\delta}{510}U.
\tag{5}
$$
以下 $Y,Z,U$ 均是这套实际物理输出，未重新归一。

置
$$
w=\left(c,\frac{1-3\delta}{60},
               \frac{-31+3\delta}{510},0,0,0\right),\qquad
v=\frac1{36}(37-3\delta,29+87\delta,-31-3\delta,0,0,0)^t.
$$
有 $wv=1$。原 $W$ 核在 $L$ 坐标中的物理收缩为
$$
\boxed{A_W=I+(\kappa-1)vw.}
\tag{6}
$$
它固定五个 $M$ 伴随、把 $W$ 乘以 $\kappa$，并且
$$
Y\circ A_W=Y+(\kappa-1)a_WW,\qquad
a_W=\frac{37-3\delta}{36}.
\tag{7}
$$
因此它确实改变被观察的 $Y$，不能作为一个只动旧伴随的操作。

## 2. 完整 CM 分支与保原输入的平移和

使用 R416 的 canonical lift
$$
\mathsf T_t^{(N)}G(z)=
 e^{-N\eta_t(z+t/2)}G(z+t).
\tag{8}
$$
对 $\alpha=\gamma_{13}^j\gamma_{19}^{\epsilon}$，
$0\le j\le17,\ \epsilon\in\{0,1\}$，定义五伴随的完整平移和
$$
\mathcal Q_\alpha^L G
=\sum_{\mathbf t\in E[\bar\alpha]^5}
 \mathsf T_{\alpha\mathbf t,\mathbf Z}^{(\mathbf N_L)}G.
\tag{9}
$$
第一轴未平移，每个 $t_\ell$ 的完整相位都按 (8) 保留。
没有用一个代表原像代替完整 trace。

R483(38) 将 $\mathbf z\mapsto\alpha\mathbf z$ 的实际拉回也保留
在来源中；把这个拉回单独写成物理单位推前，就得到等价的
完整测度式
$$
\boxed{
\nu_{(B_{13}^L)^j(B_{19}^L)^\epsilon G}
=\bar\alpha^{-5}
 [I_Y,g_\alpha I_5]_*\nu_{\mathcal Q_\alpha^L G},
\qquad g_\alpha=\alpha/\bar\alpha .
}
\tag{10}
$$
这是 R483 的同一个规范，区别仅在于将来源内的 $[\alpha]$
拉回明确移到推前上。附五伴随角分支 $\zeta\in\mu_6$ 后，
实际旧 $W$ 条件变为
$$
\boxed{W_s=cY+s\,r(\mathbf Z),\qquad s=\zeta g_\alpha.}
\tag{11}
$$
所以 (11) 的 $g_\alpha$ 不能与仍把 $[\alpha]$ 留在来源内的
R483(41) 中 $1/\bar\alpha$ 混用。

定义下列三个**固定完整来源和**：
$$
\begin{aligned}
\mathcal R_SG&=\frac1{18}\sum_{j=0}^{17}
 (-1)^j\bar\gamma_{13}^{-5j}\mathcal Q_{\gamma_{13}^j}^LG,\\
\mathcal R_{\rm new}G&=\frac1{36}
 \sum_{j=0}^{17}\sum_{\epsilon=0}^1
 \omega^{2j}(-\omega)^\epsilon
 \bar\alpha^{-5}\mathcal Q_\alpha^LG,\\
\mathcal R_HG&=\frac1{36}
 \sum_{j=0}^{17}\sum_{\epsilon=0}^1
 (-\omega^2)^\epsilon
 \bar\alpha^{-5}\mathcal Q_\alpha^LG.
\end{aligned}
\tag{12}
$$
它们只去掉 (10) 的外部伴随尺度及角平均，完整保留所有原
平移来源、CM 常数和算术权重。记
$$
\tau_{\chi,i}=\nu_{\mathcal R_\chi\mathcal F_i^L},
\qquad \chi\in\{S,{\rm new},H\}.
\tag{13}
$$
这不宣称 $\mathcal R_\chi=\mathcal C_\chi$ 作为整个联合算子。

忘掉五伴随后，(10) 的单位尺度和角平均都严格消失。
于是 R483 的完整来源身份给
$$
\boxed{
\begin{array}{c|cc}
 &Y_*\tau_{\chi,0}&Y_*\tau_{\chi,1}\\ \hline
S&\nu_{S(2z)}&c_S\nu_{S(2z)}\\
{\rm new}&0&(52/3)\nu_{S_{\rm new}}\\
H&0&c_H\nu_{H_{\rm ref}}
\end{array}
\qquad
c_S=-\frac{1+\delta}{4},\quad
c_H=-\frac{1+\delta}{2016b}.
}
\tag{14}
$$
其中 $H_{\rm ref}(0)=1$，实际曲线是 $E_{668168}$。
(14) 是完整第一边际身份；它没有给 $\tau_{\chi,i}$ 的任意
受限伴随测试赋中央零。

同样可在 $M$ 坐标中定义
$$
\mathcal R_TG=\frac16\sum_{k=0}^{5}
 \omega^{-k}\bar\gamma_{19}^{-5k}
 \mathcal Q_{\gamma_{19}^k}^M G.
\tag{15}
$$
对 $\mathcal F_+=(\mathcal F_0+\mathcal F_1)/2$，
其完整 $W$ 边际为 $6\delta T$。这里只使用边际，不将 (15)
认作 R483 完整秩一张量分解本身。

## 3. 一个固定无限 ray：付清所有平移与原 W 核的相容性

令
$$
m=13^{17}19^5,\qquad N=72m^2 .
\tag{16}
$$
取 R484 的原类
$$
\pi_0\equiv1428552127+2161889730\omega
       \pmod{712345233600},
\tag{17}
$$
并增加
$$
\boxed{\pi_0\equiv2\pmod{13^{34}},\qquad
       \pi_0\equiv1\pmod{19^{10}}.}
\tag{18}
$$
这些条件兼容；附脚本逐项做非互素 CRT，给出唯一模最小公倍数
的两坐标代表，并验证其范数为单位。新模数准确为
$$
1323133171213029144041201350687525528684869767169429257083200.
$$
(18) 约化到原 $13,19$ 条件，(17) 保其余所有已有规范。
这仍是一个固定单位 ray 类，故与 R454、R484 相同的 CM
ray-class 素理想定理给无穷多个不同普通有理素数。

在完整中心模数 $2N=144m^2$ 上，CRT 直接给
$$
\boxed{g=\pi_0/\bar\pi_0
\equiv1+90m^2+72m^2\omega.}
\tag{19}
$$
特别 $g\equiv1\pmod{2m^2}$，而 $m^2\equiv1\pmod8$。

这里不从 projective 比值猜核心的绝对标量。整个
$\mathcal S_N$ 的计算可以逐字写出。置 $k=1+N/4$，在
$Xe_j=\zeta_N^je_j,\ Ze_j=e_{j+1}$ 的原 Schrödinger 基中，
(19) 给
$$
\mathsf T_{g/N}=-X^k,\qquad
\mathsf T_{g\omega/N}=-Z^k.
$$
令 $B_Ne_j=(-1)^je_{kj+N/2}$。由于 $k^2\equiv1\bmod N$，
$B_N^2=I$，且它实现这两个完整交织。另一方面对
$t_{r,s}=(s+r\omega)/4$，
$$
\mathsf T_{t_{r,s}}^{(N)}e_j
=i^{s(j+r)}e_{j+(N/4)r}.
\tag{20}
$$
此处使用 $N/8=9m^2\equiv1\bmod4$，所以相位与 R416 相同。
对 $s$ 求和得到
$$
-B_N=\frac14\sum_{t\in E[4]}\mathsf T_t^{(N)}
       -\frac12\sum_{t\in E[2]}\mathsf T_t^{(N)}.
\tag{21}
$$
真实质量一锚 $\Theta(6mz)\in\mathcal S_N$ 的 ordinary core
是 $\beta=-\lambda$。其标准 theta 指标为
$$
\sum_{r=0}^{6m-1}e_{6mj+12mr},\qquad j=0,1.
$$
$B_N$ 置换各和中的指标并在这个子空间上为恒等，故真实
归一核心必须是
$$
\boxed{
K_N=-B_N
=\frac14\sum_{E[4]}\mathsf T_t^{(N)}
 -\frac12\sum_{E[2]}\mathsf T_t^{(N)},\qquad K_N^2=I.
}
\tag{22}
$$
这支付整个空间及全部中心，不只支付两个原状态。

### 3.1 L 平移在 M 中的准确同源 lift

(9)、(15) 的每个平移都有整数阶整除 $m$。
令 $B_6=510C_6\in M_6(\mathcal O_K)$。
其行列式与 $m$ 互素，故 $B_6^t$ 在模 $m^2$ 可逆。
给 $L$ 平移 $t=u/m$，选择
$$
v_0\equiv(B_6^t)^{-1}u\pmod{m^2},\qquad
s_M=510v_0/m.
\tag{23}
$$
则
$$
C_6^t s_M=t+m\ell,\qquad\ell\in\mathcal O_K^6.
\tag{24}
$$
附 JSON 给整个模 $m^2$ 逆矩阵并直接验证矩阵乘积为一。

实际生成函数满足
$\mathcal F_i^M(z)=\mathcal F_i^L(C_6^tz)$。
原 Hermitian Gram 身份使 (8) 的 Gaussian 和平移指数也准确
相容；(24) 唯一可能的额外常数是原标准周期 lift 的相位。
在第 $\ell$ 轴，它等于
$$
\exp\left\{\frac{N_{L,\ell}}2
  \bigl(\eta_{m\ell_\ell}t_\ell
              -\eta_{t_\ell}m\ell_\ell\bigr)\right\}.
\tag{25}
$$
$t_\ell=u_\ell/m$，故括号是 $2\pi i$ 乘整数；
所有 $N_{L,\ell}$ 都偶，(25) 恰为一。
因此 (23) 是两个原状态共用的**完整 canonical lift**。
只模 $m$ 求逆而省掉 (25) 不足以给这个断言。

在所有六轴拉回 $[m]$ 后，(23) 成为 $s_M/m\in E[m^2]^6$
的真实 Heisenberg 平移，各轴次数为 $m^2\mathbf N_M$。
它的 $W$ 分量与 (22) 的所有 $E[4]$ 平移交换：
Weil 交换因子的阶同时整除 $m^2$ 和 $4$，故只能为一。
其余五轴与 $W$ 算子本来独立。
另一方面 $[m]^*$ 与原单位处的完整 restriction/pushforward
相容，故 (3) 在这个覆盖上仍是同样的两态交换。
逐项使用 (23)–(25)，再按 (12) 求和，就得到
$$
\boxed{
\begin{aligned}
\tau_{\chi,0}|_{W\in p\mathbf Z_p}
 &=\lambda(A_W)_*\tau_{\chi,1},\\
\tau_{\chi,1}|_{W\in p\mathbf Z_p}
 &=\lambda(A_W)_*\tau_{\chi,0}.
\end{aligned}}
\tag{26}
$$
这是同一个旧物理 $W$、同一个 (6)，不是后来重新选择的核心。
覆盖尺度 $m$ 是 $p$ 单位，故可完整推回原物理坐标。
任意实际紧开条件及连续可积测试都按 (6) 运输。
对 (15) 的 $+$ 态同理得到 scalar $W$ core $\lambda$。

所有新平移在固定 $[m]$ 覆盖上都是 prime-to-$p$ 的整
Heisenberg 算子；$\bar\alpha^{-5}$、$18$、$36$ 是单位。
因此这些固定来源和及 (26) 均在原整测度格成立，不是只有
复解析函数身份。

## 4. 参考两态的非零单位质量与同核 carry

由 (14)，$\tau_{H,0}$、$\tau_{H,1}$ 的总质量分别是 $0,c_H$。
(26) 随即给
$$
\boxed{
\tau_{H,0}(W\in\mathbf Z_p^\times)=-\lambda c_H,\qquad
\tau_{H,1}(W\in\mathbf Z_p^\times)=c_H.
}
\tag{27}
$$
二者都是单位。这里没有从第一态质量零推整个联合来源为零。

对 $n\ge0$ 定义真实第一环带权
$$
f_{n,u}(y)=
 {\bf1}_{y\in p^n\mathbf Z_p^\times}
 \langle y/p^n\rangle^{du}.
\tag{28}
$$
令
$$
L_n(u)=\int f_{n,u}(Y)\,d\tau_{H,1},\qquad
J_H(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{du}\,d\nu_{H_{\rm ref}}.
$$
R483 的真实 $H_{\rm ref}$ core 为 $\beta$，质量为一，故
$$
L_n(u)=c_H\beta^n\langle\lambda^2\rangle^{ndu}J_H(u),
\qquad J_H(0)=1+\lambda.
\tag{29}
$$

现在在同一原两态上定义
$$
\begin{aligned}
I_n(u)&=\int_{W\in\mathbf Z_p^\times}
                 f_{n,u}(Y)\,d\tau_{H,0},\\
\Delta_n(u)&=\int\left[
 f_{n,u}\bigl(Y+(\kappa-1)a_WW\bigr)-f_{n,u}(Y)
                         \right]\,d\tau_{H,1},\\
F_n(u)&=I_n(u)+\lambda\Delta_n(u).
\end{aligned}
\tag{30}
$$
$\Delta_n$ 保留两个不同环带指示函数及完整 Mellin 权；
它不是把 $Y$ 固定后留下的形式差。
因为 $Y_*\tau_{H,0}=0$，按 $W$ 单位／非单位分解，再用 (26)，
得到整个 $u$ 的准确关系
$$
\boxed{F_n(u)=-\lambda L_n(u).}
\tag{31}
$$
特别 $F_n(0)=-\lambda c_H\beta^n(1+\lambda)$，这些质量不能删掉。
把 (29) 的两个环带消去同一个未知 $J'_H(0)$，得到
$$
\boxed{
\beta^{-n}F'_n(0)-F'_0(0)
 =-\lambda c_H\,n\,d\log\langle\lambda^2\rangle(1+\lambda)
 \ne0\qquad(n\ge1).
}
\tag{32}
$$
非零性与 R483(37) 相同：除 log 外显示因子均非零；
若 $\log\langle\lambda^2\rangle=0$，普通嵌入中的
$\lambda^2$ 为根单位，进而同一代数数全局也为根单位，
但它的 norm 是 $p^{-2}$，矛盾。

(32) 已将参考来源的已知非齐次项收进一个具有原两态 $W$
核心的实际来源和；没有把 $\Delta_n$ 或 $I_n$ 赋零。

对 $\chi=S,{\rm new}$ 使用同样的 (30) 定义，(26) 给
$$
F_{\chi,n}(u)=
\int f_{n,u}(Y)\,d\tau_{\chi,0}
-\lambda\int f_{n,u}(Y)\,d\tau_{\chi,1}.
\tag{33}
$$
如果三条实际秩二曲线的反证输入是
$J'_S(0)=J'_T(0)=J'_{\rm new}(0)=0$，则
$$
F'_{S,n}(0)=F'_{{\rm new},n}(0)=0\quad(n\ge0).
\tag{34}
$$
理由是 (14)、原 scalar core 及 $J_S(0)=J_{\rm new}(0)=0$；
$S(2z)$ 的 $\langle2\rangle^{du}$ 和各环带
$\langle\lambda^2\rangle^{ndu}$ 导数都乘这些零质量。
(15) 的完整 $W$ 环带中央也由 $J'_T(0)=0$ 为零。
这些已付齐次行与 (32) 的非齐次行使用同一个核心，但当前没有
证明它们之间存在消去全部实际 carry 的关系。

## 5. 原投影混管与平移和混管之间的完整差

本节把 (12) 没有保留的外部尺度准确补回。
以 $\mathcal C_\chi\mathcal F_i^L$ 为来源，任取一个仅依赖 $Y$
的连续权 $f(Y)$ 及旧深条件 $W\in p^q\mathbf Z_p$。
用 (10)、角平均展开，其积分与
$\mathcal R_\chi\mathcal F_i^L$ 上同一测试的差，恰是
$$
\boxed{
\mathcal E_{\chi,i,q}(f)=
\sum_{\alpha,\zeta}a_{\chi,\alpha,\zeta}
 \int f(Y)
 \left({\bf1}_{W_{\zeta g_\alpha}\in p^q\mathbf Z_p}
              -{\bf1}_{W_1\in p^q\mathbf Z_p}\right)
       d\nu_{\mathcal Q_\alpha^L\mathcal F_i^L}.
}
\tag{35}
$$
其中 $a_{\chi,\alpha,\zeta}$ 是 (12) 的完整该支权重再乘角平均
$1/6$。具体而言三个权重依次为
$$
\frac{(-1)^j}{108}\bar\gamma_{13}^{-5j},\qquad
\frac{\omega^{2j}(-\omega)^\epsilon}{216}\bar\alpha^{-5},\qquad
\frac{(-\omega^2)^\epsilon}{216}\bar\alpha^{-5}.
\tag{36}
$$
每个 $\zeta\in\mu_6$ 都保留。
(35) 是来源级完整相减；单位补集的差恰是其负值，
环带则取相邻两个深条件之差。
若有其他原伴随测试，也须按 (10) 同时转置，不能沿用 (35)
仅依赖 $Y$ 的简式。

### 5.1 固定有限斜率与真实交叠范围

共有固定 $216$ 个斜率
$$
\mathscr S=
\{\zeta(\gamma_{13}/\bar\gamma_{13})^j
        (\gamma_{19}/\bar\gamma_{19})^\epsilon:
 \zeta\in\mu_6,\ 0\le j\le17,\ \epsilon=0,1\}.
\tag{37}
$$
它们在 $K$ 中两两不同：两边的
$\gamma_{13},\bar\gamma_{13},\gamma_{19},\bar\gamma_{19}$
素理想赋值先确定 $j,\epsilon$，随后确定 $\zeta$。

以下给一个完全显式的固定有限坏集，不预设这些斜率在每个
普通 $p$ 都不同。对 $0\le r\le17$、$e=-1,0,1$ 及
$\zeta\in\mu_6$，置
$$
\begin{aligned}
A_{r,e}&=\gamma_{13}^r
       \gamma_{19}^{\max(e,0)}\bar\gamma_{19}^{\max(-e,0)},\\
B_{r,e}&=\bar\gamma_{13}^r
       \bar\gamma_{19}^{\max(e,0)}\gamma_{19}^{\max(-e,0)}.
\end{aligned}
$$
删去 $(r,e,\zeta)=(0,0,1)$，取所有非零整数
$$
D_{r,e,\zeta}=\operatorname{Norm}(A_{r,e}-\zeta B_{r,e}).
\tag{38}
$$
同一素理想赋值论证给 (38) 均为正。脚本实际列出其中 $303$
个不同的整数并提供其 SHA256。排除这些整数的全部素因子，
再排除 $2,3,5,7,13,17,19,349$。这是固定有限排除，不需给
尚未分解的整数猜因子；仍保 (17)–(18) 上的无穷多个 $p$。

在余下普通处，(37) 的残值两两不同，且 (5) 的 $c$ 是单位。
固定 $Y\in p^n\mathbf Z_p^\times$。若
$$
W_s\in p^{n+k}\mathbf Z_p,\qquad k\ge1,
\tag{39}
$$
则必有 $v_p(r(\mathbf Z))=n$。如果两个不同 $s,s'$ 同时满足
(39)，相减得 $(s-s')r(\mathbf Z)\in p^{n+k}$，但其赋值是
$n$，矛盾。因此这些真正的近相消管两两不交。
另外，当 $v_p(Y)\ne v_p(r(\mathbf Z))$ 时，
$$
v_p(W_s)=\min\{v_p(Y),v_p(r(\mathbf Z))\}
\quad\text{对全部 }s\in\mathscr S,
\tag{40}
$$
所以 (35) 的差在该区域逐点为零。

(39)、(40) 只支付实际管支的几何和补域位置。测度并非正测度，
故互不相交不等于这些积分不能抵消，也不允许删除 (35)。
下一接口是将 (32) 的具体同核 carry 与 (34) 及原混管的完整
差 (35) 连接；本篇没有把这一未付消元写成中央非零结论。

## 证书与依赖

- [固定 CRT、整个 quarter 比值、canonical 平移 lift 和斜率范数脚本](../scripts/check-r487-original-cm-tubes-and-common-core.py)；
  [精确数据](../scripts/check-r487-original-cm-tubes-and-common-core.json)。
- [R416：整个七十二维 quarter 核与绝对相位](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R465：原共同六输入、两态及实际坐标](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R483：原五伴随 CM 投影、三曲线行及参考环带差](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。
- [R484：原混合坐标、完整极化与既有固定 ray](R484-original-mixed-axis-common-cover-and-finite-lift-core.md)。
