# R353：完整三辅助联合来源的原输出矩投影与准确域相容性

日期：2026-11-13。**状态：已证明。** 本篇把 R348 的同一个真实 CM13 投影写成原输出 $Y$ 的显式三十次多项式矩，并将单个混合矩推广到完整三辅助联合测度。投影与所有辅助变量上的限制交换；所需权是非恒定的原 $Y$ 多项式，因此不能把这个身份当作原中央导数的新消失条件。固定曲线与无穷素数的主目标仍未完成。

## 1. 原六输入、三个辅助及真正固定来源

保留 R347–348 的全部对象：
$$
b=17,\quad E_b:y^2=x^3+b,\quad
\delta=1+2\omega,\quad \omega^2+\omega+1=0,\quad \gamma=3+\omega,
$$
$$
c=(1,2,\delta,2\delta,\gamma,\bar\gamma),\quad
r=(1,\omega^2,1,0,0,0),\quad
s=(1,0,0,-\omega^2,-\omega,0),\quad
t=(1,0,0,\omega,0,-\omega^2).
\tag{1}
$$
在同一普通周期 $\Omega=\Omega_p$ 下，
$$
\mu=-\nu_\sigma^{\otimes6}/84,\quad
Y=c^tX,\quad
U=(L_r,L_s,L_t)
=\delta^{-1}(r^*X,s^*X,t^*X),\quad
Y_*\mu=\nu_S.
\tag{2}
$$
这里 $\int e^{zX/\Omega}d\nu_\sigma=\sigma(z)$，
$\Theta=x\sigma^2$，且原 $S$ 首项为 $z^6$、质量为零。
每个 $c^tr,c^ts,c^tt$ 都等于零。

令 $\mathsf P_\Delta$ 只对三个辅助坐标同时乘同一个
$\xi\in\mu_6$ 作平均，固定 $Y$：
$$
\mathcal J_\Delta=\mathsf P_\Delta(Y,U)_*\mu.
\tag{3}
$$
也可进一步分别平均三个辅助坐标，得到 R347 的
$\mathcal J_0=\mathsf P_{\rm ind}(Y,U)_*\mu$。
以下完整六维分解对两者均成立。所有域限制均在原同一个 $p$-进坐标中。

固定来源基为
$$
F_j=\sigma^{34}x^{2+3j}
=\sigma^{30-6j}\Theta^{2+3j},\qquad 0\le j\le5.
\tag{4}
$$
它们的首阶依次为 $30,24,18,12,6,0$，首系数均为一。
每个 $F_j$ 都是原有界整测度的有限卷积来源，故给有界整测度 $\nu_{F_j}$。

## 2. 全部辅助权都在同一个六维空间

原完整变换为
$$
\mathcal F(z;u,v,w)
=-\frac1{84}\prod_{i=1}^6
 \sigma\left(c_i z+
 \delta^{-1}(\bar r_i u+\bar s_i v+\bar t_i w)\right).
\tag{5}
$$
对辅助变量取同时平均，记 $\mathcal F_\Delta$。

**命题一。** 存在唯一的六个有界辅助测度 $\tau_j$，使
$$
\boxed{\mathcal J_\Delta=\sum_{j=0}^5\nu_{F_j}\otimes\tau_j.}
\tag{6}
$$
对所有普通 $p>29$，各 $\tau_j$ 均整有界。式 (6) 对辅助变量的任意
有界连续测试成立，不只对 R347 的 $u^6v^6w^6$ 系数成立。

**证明。** 每个辅助 Taylor 系数都仍是 $z$ 的 degree 三十四 theta 截面。
完整准周期中的三个交叉项分别正比于
$\sum\bar c_i\bar r_i,\sum\bar c_i\bar s_i,\sum\bar c_i\bar t_i$，
由 (1) 全为零；没有额外的辅助 Gaussian。
同时旋转四个变量时六个 sigma 的总相位为 $\xi^6=1$，故
$$
\mathcal F(\xi z;u,v,w)
=\mathcal F(z;\xi^{-1}u,\xi^{-1}v,\xi^{-1}w).
$$
所以只在辅助变量上作同时平均，就已使 $z$ 的 $\mu_6$ 型平凡。
于是 $\mathcal F_\Delta/\sigma^{34}$ 是仅在原点有极的偶椭圆函数，
为次数至多十七的 $x$ 多项式；CM 型使幂次只能为
$2,5,8,11,14,17$。每个辅助系数均在 (4) 的同一个空间中。
这是整个 theta 截面的证明，未以有限 jet 外推无限恒等式。

为取得真正有界的系数测度，定义六个原输出矩
$$
m_k=\frac1{(6k)!\Omega^{6k}}
       (\operatorname{pr}_U)_*(Y^{6k}\mathcal J_\Delta),
       \qquad 0\le k\le5.
\tag{7}
$$
令 $B_{kj}=[z^{6k}]F_j$。矩阵 $B$ 是反三角矩阵，其反对角全为一。
故它可逆，而其逆给
$$
(\tau_0,\ldots,\tau_5)^t=B^{-1}(m_0,\ldots,m_5)^t.
\tag{8}
$$
每个 $m_k$ 都是真实有界测度的多项式权 pushforward，因而有界。
当 $p>29$ 时全部 $(6k)!$ 与 $\Omega$ 都是单位；$F_j$ 的整有界性
又使 $B_{kj}$ 整，故 $B^{-1}$ 也整，得到所述整性。

对每个辅助单项式，(8) 与已证六维空间给全部 $Y$ 矩恒等式。
$p$-进多变量多项式在连续函数中稠密（逐变量用 Mahler 展开），
有界测度由这些矩唯一确定，所以得到整个联合测度 (6)。同样论证适用于
分别平均的 $\mathcal J_0$。$\square$

因而任何有界辅助函数 $h(U)$ 都给原输出来源
$$
Y_*(h(U)\mathcal J_\Delta)=
       \sum_{j=0}^5\tau_j(h)\nu_{F_j}.
\tag{9}
$$
特别，辅助变量的 clopen 域限制保持整个六维来源空间。

## 3. 同一个 CM13 投影的有限原矩实现

R348 已在整个原六维空间证明
$$
\Pi_{S,b}(F)=\ell_b(F)S,\qquad
\ell_b\left(\sum v_jF_j\right)
=\sum_{j=0}^5\ell_jb^{j-4}v_j,
$$
$$
(\ell_0,\ldots,\ell_5)
=\frac1{17496}(-329,14,112,-616,7168,-15232).
\tag{10}
$$
这是原 $M=[4+\omega]_*[4+\omega^2]^*$ 的同一个准确投影，
不是新指定的本征线。

存在唯一六个有理数 $q_0,\ldots,q_5$，使对整个六维空间
$$
\boxed{\ell_b(F)=\sum_{k=0}^5q_kb^{1-k}[z^{6k}]F.}
\tag{11}
$$
其完整数值如下。

| $k$ | $q_k$ |
|---|---|
| 0 | $\frac{-2069648}{2010516036890625}$ |
| 1 | $\frac{357920889095025281}{1018081875447511875}$ |
| 2 | $\frac{-77609837953}{2948013943875}$ |
| 3 | $\frac{9335159}{1970268300}$ |
| 4 | $\frac{-629}{65610}$ |
| 5 | $\frac{-329}{17496}$ |

这组数的分母素因子全部在
$\{2,3,5,7,11,13,19,23,29\}$ 中。

### 3.1 完整可复现的有理计算

只需先取 $b=1$。令 $T=z^6$，
$$
x=z^{-2}X(T),\quad X(T)=\sum_{n\ge0}w_nT^n,\quad
\sigma=z\exp A(T),\quad A(T)=\sum_{n\ge1}a_nT^n.
$$
原方程 $x''=6x^2$、$y^2=x^3+1$ 及 $(\log\sigma)''=-x$ 给
$$
w_0=1,\quad w_1=-1/7,\quad
w_n=\frac{6\sum_{i=1}^{n-1}w_iw_{n-i}}
                  {(6n-2)(6n-3)-12}\ (n\ge2),\qquad
a_n=-\frac{w_n}{6n(6n-1)}.
\tag{12}
$$
于是
$$
F_j=T^{5-j}\exp(34A(T))X(T)^{2+3j}.
\tag{13}
$$
只取 $0\le n\le5$，因更高项不可能影响 (11) 的六个矩。
设 $B_{kj}$ 为 (13) 的 $T^k$ 系数，依 $j=0,\ldots,5$ 解
$$
q_{5-j}=\ell_j-\sum_{k=6-j}^5q_kB_{kj}.
\tag{14}
$$
反对角是一，故 (14) 无任意选择，逐项给上表。
附带的纯 BigInt 有理数脚本直接输出全部 $B$、$q$ 并验证六个
$\sum_kq_kB_{kj}=\ell_j$。这验证的是已证明六维空间中的完整线性算子，
不依赖目标素数样本。

一般 $b$ 的规范满足
$F_{j,b}(z)=b^{j-5}F_{j,1}(b^{1/6}z)$，所以第 $6k$ 阶系数乘
$b^{j-5+k}$。再乘 (11) 中 $b^{1-k}$，恰为 (10) 的 $b^{j-4}$，
支付了所有尺度。

## 4. 完整三辅助投影测度

在原 $Y$ 上定义准确权
$$
\boxed{
Q_{b,p}(Y)=\sum_{k=0}^5
 q_k b^{1-k}\frac{Y^{6k}}{(6k)!\Omega^{6k}}.
}
\tag{15}
$$
对所有普通 $p>29$，它是一个整、有界、$\mu_6$ 不变的多项式权。
定义原辅助测度
$$
\boxed{
\tau_\Delta=(\operatorname{pr}_U)_*
                   (Q_{b,p}(Y)\mathcal J_\Delta).
}
\tag{16}
$$
由 (6)、(10)、(11) 得
$$
\boxed{
(\Pi_{S,b}\otimes1)\mathcal J_\Delta
                   =\nu_S\otimes\tau_\Delta.
}
\tag{17}
$$
这是原同一个 CM13 投影在完整联合测度上的身份。
全部原输出，包括 $Y\in p\mathbf Z_p$，都留在 (15)–(17) 中。

每个有界辅助函数 $h$ 都满足
$$
\boxed{
\Pi_{S,b}\bigl(Y_*(h(U)\mathcal J_\Delta)\bigr)
      =\tau_\Delta(h)\nu_S.
}
\tag{18}
$$
因此该有限原投影与任意辅助域限制交换；无需把限制域的指示函数
替换为某个有限 Taylor 截断。对同时 $\mu_6$ 不变的 $h$，
右边的标量直接就是原六输入积分
$\int h(U)Q_{b,p}(Y)d\mu$，因为 (15) 也 $\mu_6$ 不变。

同样设
$\tau_0=(\operatorname{pr}_U)_*(Q_{b,p}(Y)\mathcal J_0)$，
则 $\tau_0=\mathsf P_{\rm ind}\tau_\Delta$。
由 (2) 和 $\ell_b(S)=1$，
$$
\boxed{\tau_\Delta(\mathbf Z_p^3)=\tau_0(\mathbf Z_p^3)=1.}
\tag{19}
$$
此外，忽略第三辅助坐标后，R344 给
$(Y,L_r,L_s)_*\mathcal J_0=\nu_S\otimes\Xi$。
对其第一坐标施加 (15)，即得
$$
\boxed{(\operatorname{pr}_{L_r,L_s})_*\tau_0=\Xi.}
\tag{20}
$$
这是同一个实际相关双辅助测度，没有将其拆成独立边缘的乘积。

## 5. 一个准确的三辅助混合矩

对 $h=L_r^6L_s^6L_t^6$，两种辅助平均都不改变积分。
R348 给原加权来源
$$
Y_*(h\,\mu)
=-\frac{(6!)^3\Omega^{18}}{84}\nu_G,\qquad
\ell_b(G)=-\frac{539+1120\omega}{2952450}b^3.
$$
因此 (16) 完整给
$$
\boxed{
\tau_\Delta(L_r^6L_s^6L_t^6)
=\tau_0(L_r^6L_s^6L_t^6)
=\frac{2560}{1701}(539+1120\omega)b^3\Omega^{18}.
}
\tag{21}
$$
其常数来自 $(6!)^3/(84\cdot2952450)=2560/1701$，
没有遗漏原 $-1/84$ 或周期。
由 $N(539+1120\omega)=3\cdot7^2\cdot19\cdot337$，
对所有普通 $p>29$、$p\ne337$，(21) 为单位。
这里陈述的是实际辅助测度的全质量矩，不是原输出单位域上的中央导数。

## 6. 非恒定权及限制域的准确边界

权 (15) 的最高系数准确为
$$
\boxed{
[Y^{30}]Q_{b,p}
=-\frac{47\,b^{-4}\Omega^{-30}}
 {662980576467727823128693309440000000}.
}
\tag{22}
$$
显示分母只含不大于二十九的素数。四十七是惰性素数，
所以对每个普通 $p>29$，(22) 是单位。
对 $p>31$，$Q_{b,p}\bmod p$ 的次数三十严格小于 $p-1$；
故它在 $\mathbf F_p^\times$ 上不可能是常数：
否则减去该常数会有 $p-1>30$ 个根，而最高系数非零。

因此，(16) 并没有把三辅助观察无权地化为 $\nu_S$ 的外积。
它精确显示了原输出上必须支付的固定非恒定多项式权。
例如对任何有界原单位输出中央函数 $f_p(Y)$，完整分解只是
$$
\int f_p(Y)h(U)\,d\mathcal J_\Delta
=\tau_\Delta(h)\int f_p\,d\nu_S
+\int f_p(Y)h(U)\,d\mathcal J_\perp,
$$
$$
\mathcal J_\perp=
\mathcal J_\Delta-\nu_S\otimes\tau_\Delta,\qquad
(\Pi_{S,b}\otimes1)\mathcal J_\perp=0.
\tag{23}
$$
即使原完整中央导数为零，(23) 的补项也必须保留。

同样，若再限制六个原输入或 R339 的独立叶变量，
其输出来源未必仍在 (4) 的六维空间中。此时 (15) 仍定义一个真正
有界加权 pushforward，但不能在未证明来源闭合前，将它认作同一个
CM13 截面算子。式 (18) 的适用范围是已经支付的辅助坐标函数，
不是任意叶输入的指示函数。

本篇支付的是 R348 所需“完整三辅助来源及辅助域”的准确相容性。
下一步仍须将 (23) 的原补项或 (15) 的真实输出权，同 R350 的
完整叶深度补域一起控制；没有新增未经证明的中央零。

## 证书与依赖

- [R347：三个原辅助坐标、单位矩及六维来源](R347-three-original-auxiliaries-and-a-unit-remaining-source.md)。
- [R348：完整原来源与同一 CM13 投影](R348-complete-three-auxiliary-source-and-original-cm13-projection.md)。
- [R344：原相关双辅助测度](R344-overlapping-original-pair-full-torsion-factorization-and-contracting-kernel.md)。
- [R350：单相位原碰撞管及完整叶补域](R350-original-diagonal-pair-six-phase-collision-and-leaf-complement.md)。
- [纯有理数证书](../scripts/check-jzero-full-three-auxiliary-output-moment-projector.js)：
  只执行 (12)–(14) 的六阶有限有理运算，完整回验 (10)。
  已在本会话的 JavaScript BigInt 运行时执行；未声称失联的终端执行了脚本，
  没有扫描任何目标素数。环境不可用期间仅通过允许的小文本接口发表。
