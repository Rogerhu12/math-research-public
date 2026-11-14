# R208 第二附录：单个高位反射的范数配对界

日期：2026-11-12（UTC）。作者：critical_kernel。

状态：完整实际估计。本文将 R208 的强交换子机制加强为单个高位反射的核间范数配对界。该界保留全部低位进位，只把同位主项放进一个实际范数代数单位。它不证明核投影与该反射在范数中渐近交换，也不自动给多个高位反射乘积的相同结论。

## A. 结论

沿用 R208 的真实闭算子
$$
X=a_*I+\sum_{k\ge0}a_kV_k,\qquad
\mathcal B_2=\sum_{k\ge0}a_k^2(I-V_k^2),\qquad
Y=\varphi(\mathcal B_2),\qquad
T=X-Y,
$$
其中 $a\in\ell^2$，$\varphi$ 在 $0$ 邻域全纯。
记
$$
M=\ker T,\qquad
J_j=M_{\chi_j},\qquad
g=\|a\|_2,\qquad \eta_*=\sup_k\eta_k<1/4.
$$
$J_j$ 为自伴酉算子，并且 $CJ_jC=-J_j$。

**定理。** 存在只依赖固定行 $a$、固定全纯分支 $\varphi$ 和实际模型的常数 $C_*$，
使对每个充分大且 $a_j\ne0$ 的 $j$，
$$
\boxed{
\|P_{CM}J_jP_M\|
=\|P_MJ_jP_{CM}\|
\le C_*\frac{\eta_{j-1}}{|a_j|}.
}
\tag{A.1}
$$
等价地，
$$
|B(u,J_jv)|
\le C_*\frac{\eta_{j-1}}{|a_j|}\|u\|\,\|v\|
\qquad(u,v\in M).
\tag{A.2}
$$

(A.1) 不需要先用 R208 得到 $M$ 全等向。
对不可绝对求和的 $\ell^2$ 行，可以选子列使右边任意快地趋于零；
对通常慢规则尾，它给超快小量。

## B. 单位反射的准确域和相对进位式

记 $\gamma_j(B)=J_jBJ_j$。
由于 $V_k$ 只作用尾位 $[k,\infty)$，当 $k>j$ 时
$$
\gamma_j(V_k)=V_k.
$$
所以 $\gamma_j(X)-X$ 在有限柱核心上只有有限个有界项。
$J_j$ 保持该核心。
如 R208 第4节的闭图逼近，并反向使用 $J_j^2=I$，得到
$$
J_j\operatorname{Dom}X=\operatorname{Dom}X,\qquad
\gamma_j(X)=X+\delta_jX
$$
在同一真实域上成立，其中 $\delta_jX$ 是那个有界有限和。
因此 $\gamma_j(T)$ 与 $T$ 同域。

单物理位反射使 $E_j,E_j^*$ 同时变号，而固定高尾。
实际进位给
$$
\gamma_j(N_j)=-N_j.
\tag{B.1}
$$
对 $k<j$，令 $R_{kj}=E_k^*\cdots E_{j-1}^*$。
R208 的有限真实链分解为
$$
N_k=N_k^{[j]}+\frac{\alpha_j}{\alpha_k}R_{kj}N_j.
$$
因此
$$
\gamma_j(N_k)-N_k
=-2\frac{\alpha_j}{\alpha_k}R_{kj}N_j.
\tag{B.2}
$$
所有这里的低头因子与 $N_j$ 交换。
此外 $\gamma_j(N_k)$ 也与 $N_j$ 交换，
这可由原来的 $[N_k,N_j]=0$ 和 (B.1) 直接共轭验证。

利用 $V_k=2(I+N_k)^{-1}-I$ 和真实逆差恒等式，
$$
\gamma_j(V_k)-V_k=N_jC_{kj},
$$
$$
C_{kj}
=4\frac{\alpha_j}{\alpha_k}
(I+\gamma_j(N_k))^{-1}R_{kj}(I+N_k)^{-1}.
\tag{B.3}
$$
$C_{kj}$ 与 $N_j$ 交换，且
$$
\boxed{\|C_{kj}\|\le36\alpha_j/\alpha_k.}
\tag{B.4}
$$
这是在除去 $N_j$ 后仍有小范数的实际因子式，不是形式除法。

同位的准确式为
$$
\gamma_j(V_j)-V_j
=4N_j(I-N_j^2)^{-1}.
$$
于是
$$
\boxed{
\delta_jX
=N_j\left[4a_j(I-N_j^2)^{-1}+C_j^{\rm low}\right],
}
\tag{B.5}
$$
$$
C_j^{\rm low}=\sum_{k<j}a_kC_{kj},\qquad
\|C_j^{\rm low}\|
\le\frac{36g\,\eta_{j-1}}{\sqrt{1-\eta_*^2}}.
\tag{B.6}
$$
所有括号内的项都与 $N_j$ 交换。

## C. Bell 项的同位主项与低位误差

对同位项，$V_j$ 与 $\gamma_j(V_j)=V_j^{-1}$ 都是 $N_j$ 的有理函数。
直接计算
$$
V_j^{-2}-V_j^2
=8N_j(I+N_j^2)(I-N_j^2)^{-2}.
$$
故
$$
\boxed{
\gamma_j(\mathcal B_2)-\mathcal B_2
=N_j(Q_j+E_j^{\rm low}),
}
\tag{C.1}
$$
其中
$$
Q_j=-8a_j^2(I+N_j^2)(I-N_j^2)^{-2}\in\mathcal A.
\tag{C.2}
$$
因为 $\|N_j^2\|=\eta_j\le\eta_*<1/4$，
$$
\|Q_j\|\le32|a_j|^2.
\tag{C.3}
$$

低位误差可明确写为
$$
E_j^{\rm low}
=-\sum_{k<j}a_k^2
\left(C_{kj}\gamma_j(V_k)+V_kC_{kj}\right).
$$
它与 $N_j$ 交换。由 $\|V_k\|,\|\gamma_j(V_k)\|\le6$，
$$
\boxed{\|E_j^{\rm low}\|\le432g^2\eta_{j-1}.}
\tag{C.4}
$$
虽然 $C_j^{\rm low},E_j^{\rm low}$ 一般不在 $\mathcal A$ 中，
它们的范数与相对 $N_j$ 的真实因子式已经完全受控。

## D. 全纯差的二次分拆

记 $B=\mathcal B_2$，并定义只保留同位变化的
$$
\widehat B_j=B+N_jQ_j\in\mathcal A.
\tag{D.1}
$$
其字符为零，所以谱仍为 $\{0\}$。
另一方面
$$
\gamma_j(B)-\widehat B_j=N_jE_j^{\rm low}.
$$

为 $\varphi$ 取 R208 使用的固定圆周 $\Gamma$，
并记
$$
R_\Gamma=\max_{z\in\Gamma}\|(z-B)^{-1}\|.
$$
由于 $\|N_jQ_j\|\to0$，对充分大 $j$，
$$
\max_\Gamma\|(z-\widehat B_j)^{-1}\|\le2R_\Gamma.
$$
$\gamma_j(B)$ 与 $B$ 酉等价，所以其对应 resolvent 范数恰等于原范数。
可固定
$$
C_\Gamma=\frac{\operatorname{length}\Gamma}{2\pi}
\max_\Gamma|\varphi(z)|\,2R_\Gamma^2.
$$

两次真实全纯差恒等式给
$$
\varphi(\widehat B_j)-\varphi(B)=N_jK_j,
\tag{D.2}
$$
$$
K_j=\frac1{2\pi i}\int_\Gamma
\varphi(z)(z-\widehat B_j)^{-1}Q_j(z-B)^{-1}\,dz.
$$
这里
$$
\boxed{K_j\in\mathcal A,\qquad \|K_j\|\le32C_\Gamma|a_j|^2.}
\tag{D.3}
$$
它是实际有界的全纯差商；没有把 $N_j^{-1}$ 当作全域有界算子。

类似地，
$$
\varphi(\gamma_j(B))-\varphi(\widehat B_j)=N_jF_j,
\tag{D.4}
$$
$$
F_j=\frac1{2\pi i}\int_\Gamma
\varphi(z)(z-\gamma_j(B))^{-1}
E_j^{\rm low}(z-\widehat B_j)^{-1}\,dz,
$$
并且
$$
\boxed{\|F_j\|\le432C_\Gamma g^2\eta_{j-1}.}
\tag{D.5}
$$
在 (D.2)、(D.4) 中，所有相关 resolvent 都与 $N_j$ 交换，
因此把 $N_j$ 提到左侧完全合法。
$\varphi(\gamma_j(B))=\gamma_j(Y)$，故
$$
\boxed{\delta_jY=N_j(K_j+F_j).}
\tag{D.6}
$$

## E. 一个保核的单位与一个不必保核的小误差

对 $a_j\ne0$，定义
$$
U_j=(I-N_j^2)^{-1}-\frac{K_j}{4a_j}\in\mathcal A,
$$
$$
G_j=\frac{C_j^{\rm low}-F_j}{4a_j}.
$$
(B.5)、(D.6) 合起来给准确等式
$$
\boxed{\gamma_j(T)-T=4a_jN_j(U_j+G_j).}
\tag{E.1}
$$

由 (D.3)，
$$
\|U_j-I\|
\le\frac{\eta_j}{1-\eta_j}+8C_\Gamma|a_j|
\longrightarrow0.
$$
所以对全部充分大且 $a_j\ne0$ 的 $j$，
$$
U_j^{-1}\in\mathcal A,\qquad \|U_j^{-1}\|\le2.
\tag{E.2}
$$
R125 的完整域交换与 $Y\in\mathcal A$ 使 $U_j$ 和其逆都保持 $M$，
故 $U_jM=M$。

误差则满足
$$
\boxed{
\|G_j\|
\le
\left(\frac{9g}{\sqrt{1-\eta_*^2}}+108C_\Gamma g^2\right)
\frac{\eta_{j-1}}{|a_j|}.
}
\tag{E.3}
$$
$G_j$ 不必保持 $M$；下面不作这种假设。

## F. 跨核配对与稠密像取消

由 $CJ_jC=-J_j$，$\gamma_j(T)$ 仍为 $C$ 自伴；
它的核是 $J_jM$。
两个闭算子同域，所以对 $u\in M$、$w\in J_jM$，
$$
B((\gamma_j(T)-T)u,w)=0.
\tag{F.1}
$$
代入 (E.1)，用 $N_j$ 的双线性对称性，得到
$$
B((U_j+G_j)u,N_jw)=0.
$$

$M$ 对 $A$ 不变，故 R23 给 $\overline{N_jM}=M$。
又 $N_jJ_j=-J_jN_j$，因此
$$
\overline{N_j(J_jM)}=J_jM.
$$
由连续性，(F.1) 因而推出
$$
B((U_j+G_j)u,w)=0
\qquad(u\in M,\ w\in J_jM).
\tag{F.2}
$$
这里取消的是有准确稠密像依据的 $N_j$，不是未知慢一阶分母。

对任意 $x,v\in M$，在 (F.2) 中取 $u=U_j^{-1}x$、$w=J_jv$，
可得
$$
B(x,J_jv)=-B(G_jU_j^{-1}x,J_jv).
$$
因此
$$
|B(x,J_jv)|\le2\|G_j\|\|x\|\,\|v\|.
$$
结合 (E.3)，定理成立，例如可取
$$
\boxed{
C_*=\frac{18g}{\sqrt{1-\eta_*^2}}+216C_\Gamma g^2.
}
\tag{F.3}
$$

## G. 系数后果和准确边界

对 $u,v\in M$，令
$$
h_{u,v}(y)=u(y)v(-1-y)\in L^1.
$$
由于 $\chi_j(-1-y)=-\chi_j(y)$，(A.2) 等价于其单比特 Walsh 系数满足
$$
|\widehat h_{u,v}(\{j\})|
\le C_*\frac{\eta_{j-1}}{|a_j|}\|u\|\,\|v\|.
\tag{G.1}
$$
R208 另外给这些乘积的常数系数为零。

若在某个尾指标集 $I$ 上
$$
\sum_{j\in I}\left(\frac{\eta_{j-1}}{|a_j|}\right)^2<\infty,
$$
则相应的一阶系数平方和有统一的双线性界。
这不等于声称整个 $h_{u,v}$ 属于 $L^2$。

对每个 $a\in\ell^2\setminus\ell^1$，
R208 的子列论证还允许按任意预给的趋零阈值递归选位，
故总能在一个无限子列上使 (A.1) 的右端可和。
但本证明没有把该子列扩大为全部指标，也没有处理零系数位置的除法。

(A.1) 控制的是 $M$ 到 $CM$ 的一个交叉压缩。
$M\oplus CM$ 未被证明等于全空间，
所以不能把它写成 $\|[P_M,J_j]\|\to0$。

更不能把单比特估计直接乘起来得到所有有限集 $F$ 的
$B(M,J_FM)$ 控制。
单次消去用到了 $N_jJ_j=-J_jN_j$、
同位主项产生的 $\mathcal A$ 单位、以及该单位保持原核 $M$。
多个不同位翻转的相对因子不自动保留这三个性质；
中间目标空间也不再是本节固定的两个核。
一般慢平方核仍未被排除。
