# R150 附录：三维第三矩的二次差分与长度四共同支撑归约

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明的条件归约。** 本文针对原第三普通矩 $T_3$ 的本质支撑恰为三维、且一次矩不在曲线二点割线簇中的情况。先从原 Hankel 差分证明前三阶累积量共同支撑至多四维；若一次矩在三次矩本质支撑之外，则这个四维空间必为准确长度四的曲线 jet 支撑。对四个不同点且下述四个线性值非零的子类，再得到一个明确的半权分割必要条件。不排除其余均值、零线性值或重 jet。

## 1. 二次曲线理想及一个线性代数事实

记 $C=\{[v(s)]:s\in\mathbb P^1\}\subset\mathbb P^5$，原齐次曲线是
$$
v_{\mathrm{hom}}(a,b)=(a^5,a^4b,\ldots,b^5).
$$
令 $\mathcal I_2$ 为所有在该曲线上为零的二次式。写 $q(r)=r^{\mathsf T}Qr$，其中 $Q$ 为复对称矩阵。原 Hankel 矩阵空间恰为这些 $Q$ 在迹配对下的零化子：$q(v(s))=0$ 等价于 $Q$ 每条反对角线的系数和为零。

固定非零 $y\in\mathbb C^6$，置
$$
U_y=\operatorname{span}\{Qy:q\in\mathcal I_2\}.
\tag{1.1}
$$
以下全秩条件是本文的明确假设：
$$
\boxed{\operatorname{rank}(y_{j+k})_{0\le j\le3,\ 0\le k\le2}=3.}
\tag{1.2}
$$
这正是排除长度至多二的射影曲线 jet 表示；其有限 apolar 证明见[非零一次矩、第三矩零的分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)。此处只需要显示的秩条件。

**引理。** 在 (1.2) 下，$U_y=\mathbb C^6$。

**证明。** 若 $z$ 与全部 $Qy$ 在复双线性配对下正交，则 $yz^{\mathsf T}+zy^{\mathsf T}$ 是 Hankel。记前、后五项为 $Y_0,Y_1$ 和 $Z_0,Z_1$，得到
$$
Y_1\wedge Z_0=Y_0\wedge Z_1.
$$
(1.2) 保证 $Y_0,Y_1$ 独立。逐次楔乘它们，得到
$$
Z_0=\alpha Y_0+\beta Y_1,\qquad
Z_1=\gamma Y_0-\alpha Y_1.
$$
四个重叠坐标给
$$
\beta y_{j+2}+2\alpha y_{j+1}-\gamma y_j=0
\quad(0\le j\le3).
$$
由 (1.2)，$\alpha=\beta=\gamma=0$，所以 $z=0$。零化子为零便证明引理。$\square$

## 2. 原第三矩的完整二次差分

仍写原物理张量
$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)(r^{\mathsf T}Hr)+4V(r,r,r),
\quad H_{ij}=H_{i+j},\quad V_{ijk}=V_{i+j+k}.
$$
对任意 $q(r)=r^{\mathsf T}Qr\in\mathcal I_2$，Hankel 性给
$$
q(\partial_r)(r^{\mathsf T}Hr)=0,
\qquad q(\partial_r)V(r,r,r)=0.
$$
对第一、二项直接求导，准确得到一次式对应的向量身份
$$
\boxed{
\frac16q(\partial_r)T_3
=(y^{\mathsf T}Qy)y-4HQy
=-4MQy,\qquad M=H-\tfrac14yy^{\mathsf T}.
}
\tag{2.1}
$$
(2.1) 是对全部原物理二次关系的完整身份；没有假设 $M$ 本身是 Hankel。

令 $W$ 为 $T_3$ 的本质支撑，即唯一最小的线性子空间，使 $T_3\in\operatorname{Sym}^3 W$。假设
$$
\dim W=3.
\tag{2.2}
$$
一个由 $W$ 支撑的三次式的全部二阶导数都在 $W$ 内。由 (2.1) 和 §1 引理，
$$
\boxed{\operatorname{Ran}M\subseteq W.}
\tag{2.3}
$$
因 $M$ 对称，它由 $W$ 内的二阶张量表示。于是
$$
E=W+\mathbb Cy,\qquad \dim E\le4
$$
同时支撑 $y$ 和 $H=M+yy^{\mathsf T}/4$。又
$$
\boxed{
V(r,r,r)=\tfrac14T_3(r)+\tfrac18(y^{\mathsf T}r)^3
          +\tfrac32(y^{\mathsf T}r)M(r,r),
}
\tag{2.4}
$$
所以 $V$ 也由 $E$ 支撑。这一步从单个三次矩的本质支撑导出了前三个累积量的共同支撑；只在已明示的 (1.2) 假设下成立。

## 3. 一次矩在 W 之外时，四维共同支撑必为曲线 jets

现在再假设 $y\notin W$，故 $E=W\oplus\mathbb Cy$ 四维。先证明 $V$ 的本质支撑就是整个 $E$。

设一个线性方向 $\ell\in E^*$ 湮灭 $V$ 的一阶导数，记 $\alpha=\ell(y)$，$\ell_W=\ell|_W$。在 (2.4) 中，按独立变量 $y^{\mathsf T}r$ 的次数比较：二次项系数为 $3\alpha/8$，所以 $\alpha=0$。剩下一次项迫 $D_{\ell_W}M=0$，常数项迫 $D_{\ell_W}T_3=0$。由于 $W$ 是本质支撑，后一式迫 $\ell_W=0$。因此 $\ell=0$，而 $V$ 的本质维数确为四。

原 $V$ 的一阶展平矩阵为 $V_{i+j+k}$。合并重复的列键 $j+k$ 后，正是
$$
\mathsf V=(V_{i+n})_{0\le i\le5, 0\le n\le10}.
$$
一阶展平秩等于三次张量本质维数，故
$$
\operatorname{rank}\mathsf V=4.
\tag{3.1}
$$

定义有限配对 $\Lambda_V:S_{15}\to\mathbb C$，以 $V_0,\ldots,V_{15}$ 为其单项式值。仍令 $I_k$ 为全部互补次数配对的核、$b_k=\dim S_k/I_k$。有 $b_k=b_{15-k}$，且首次非零 $I_a$ 后 $b_k$ 不增；两移位维数引理的证明与前稿相同。

由 $b_5=4<6$ 知 $a\le5$。另一方面
$$
b_{a-1}=a=b_{16-a},\qquad
 a\ge b_5\ge b_{16-a}=a,
$$
所以 $a=4$，且 $I_4$ 恰一维。唯一四次关系 $g$ 使 $\Lambda_V$ 杀掉 $gS_{11}$。四维有限商的除法与中国剩余定理给准确总长度四的曲线 jet 表示；每个最高 jet 系数非零，否则产生较低次数关系，矛盾。

其 jet 向量的张成空间恰为 $V$ 的一阶展平像，即 $E$。所以
$$
\boxed{E\text{ 是一个准确长度四的曲线 jet 空间，含全部重根与}\ \infty.}
\tag{3.2}
$$
无正性、非退化首主块或无限矩延拓假设。

## 4. 四个不同支撑点：中央三次矩的明确形式

本节只处理 (3.2) 中四个不同点的子类。取对应独立曲线代表 $u_1,\ldots,u_4$，则
$$
V=\sum_{i=1}^4 v_i u_i^{\otimes3},\qquad v_i\ne0.
$$
定义唯一 $\lambda\in E^*$，使 $\lambda|_W=0$、$\lambda(y)=1$，并记 $l_i=\lambda(u_i)$。从 (2.4) 分别沿 $\lambda$ 求一、二、三阶导数，得到
$$
\boxed{H=2V(\lambda,\cdot,\cdot),\qquad
 y=8V(\lambda,\lambda,\cdot),\qquad
 V(\lambda,\lambda,\lambda)=1/8.}
\tag{4.1}
$$
这里前两个等式也可在含重 jets 的 (3.2) 中使用。

若进一步 $l_i\ne0$ 对全部 $i$ 成立，置
$$
w_i=8v_i l_i^3,\qquad x_i(r)=\frac{u_i^{\mathsf T}r}{l_i},\qquad
\mu(r)=\sum_iw_ix_i(r).
$$
由 (4.1)，$w_i\ne0$、$\sum_iw_i=1$，且
$$
y^{\mathsf T}r=\mu(r),\quad
H(r,r)=\frac14\sum_iw_i x_i(r)^2,\quad
V(r,r,r)=\frac18\sum_iw_i x_i(r)^3.
$$
于是完整第三矩恰为
$$
\boxed{
T_3(r)=\frac12\sum_{i=1}^4w_i\bigl(x_i(r)-\mu(r)\bigr)^3.}
\tag{4.2}
$$
这些 $w_i$ 是复数代数参数，不是概率权；“中央”只描述显示的代数恒等式。

## 5. 完整临界性强迫某组复权之和为二分之一

现在额外使用原完整临界性的最高矩必要条件
$$
T_3(Kv(z))\equiv0.
$$
由[三维最高矩投影分类](R150-appendix-highest-moment-essential-support-and-cubic-projection-types.md)，非零三元三次式要么为不可约二次式乘一次式，要么是物理有理曲线的不可约三次方程。因此它的射影平面三次曲线必奇异。

这里可以不依赖未说明的光滑性结论：二次式和一次式必在复射影平面相交，交点使乘积梯度为零。若是不可约三次，光滑平面三次具有非零正则微分，仿射式为 $dx/C_y$，在其余图中由隐式微分改写，次数三使它也在无穷远正则。将其拉回非恒定的物理 $\mathbb P^1$ 参数化，得到非零正则微分，矛盾：$\mathbb P^1$ 上的有理微分若在所有有限点正则，便为多项式乘 $dt$，在无穷远正则又迫该多项式为零。因此不可约三次同样必须奇异。

在 (4.2) 中令 $z_i=x_i-\mu$。三维本质变量空间是
$$
\sum_iw_i z_i=0,
$$
而三次式为 $\tfrac12\sum_iw_i z_i^3$。其射影奇异点的拉格朗日乘子方程是
$$
w_i z_i^2=\beta w_i\quad(1\le i\le4).
$$
因为 $w_i\ne0$，有 $z_i^2=\beta$。若 $\beta=0$，所有 $z_i=0$，不是射影点。因此可共同缩放，使每个 $z_i=\varepsilon_i\in\{1,-1\}$。原超平面条件成为
$$
\sum_i\varepsilon_i w_i=0.
$$
结合 $\sum_iw_i=1$，准确得到
$$
\boxed{\text{存在非空真子集 }A\subset\{1,2,3,4\},\qquad
\sum_{i\in A}w_i=\sum_{i\notin A}w_i=\tfrac12.}
\tag{5.1}
$$
反过来，这种分割确实给该中央三次曲线的奇异点；但它不自动给原完整临界性。

## 6. 未覆盖部分

共同支撑降到至多四维使用 (1.2)；mean 落在二点割线簇时不自动成立。准确长度四还要求 $y\notin W$。式 (5.1) 另要求四个不同支撑点和全部 $l_i\ne0$；其余长度四重 jet 或零 $l_i$ 尚须另算。即使这些假设全部满足，低阶原梯度及最高多项式恒等式仍未由 (5.1) 代替。

本文没有把两个已付平面之外的三维支撑全部排除，没有证明原三匹配方向在全临界集上消失，也没有给全局自然幂证书或实际算子逆。后续可在显示的长度四局部代数中继续完整梯度，而不必猜测所有矩天然共用第三矩支撑。
