# 同一最大除法图源的两个实际 dyadic 边界量

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本稿准确边界分解及两型全 carry 预算已证明；一般来源的边界极限仍未支付。**
接原 [闭关系与两个范围核心](../results/R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)。本稿对同一个最大图来源写出一条明确截断的准确图误差。N 型是两个正交项的恒等式；Y 型也保留全部 Cayley 逆，并把它们相对真实有限头的误差统一支付为 $12e^{-760\,16^{r-1}}\|y\|$。
这不是整个图核心定理：另一条逼近序列可能比这里的前缀截断更好。

## 1. 固定同一来源

所有原 $B,S=B^*,T_N,T_Y,a_i,\alpha_i,d_i,\mathsf N_i$ 及 $G_0=TJ_B$ 仍如前稿。
取一个实际最大图对
$$
y\in\mathcal D(G_0^*),\qquad f=G_0^*y\in\mathcal H.
$$
于是 $T^*y=Sf$，且 $y_0=0$。
令 $h$ 为唯一形式向量
$$
Sh=y.
$$
在有限输出坐标中取消单射前移 $S$，得到准确形式等式
$$
T^*h=f.
\tag{1.1}
$$
不假定 $h\in\mathcal H$。

固定 $r\ge1$、$d=2^r$。按低 $r$ 位写
$$
h=\sum_{\ell=0}^{d-1}e_\ell\otimes h_\ell,
\qquad Q_r=e_{d-1}\otimes e_{d-1}^*\otimes I,
$$
$$
h^{<r}=(I-Q_r)h.
$$
当 $\ell<d-1$ 时，首零位小于 $r$，故 $Sh\in\mathcal H$ 保证 $h_\ell\in\mathcal H_{\rm tail}$，并且
$$
\boxed{
h^{<r}\in\mathcal H,
\qquad \|h^{<r}\|\le\alpha_{r-1}^{-1}\|y\|.
}
\tag{1.2}
$$
定义同一个尾向量 $y_r$ 和输出顶行 $f_r$：
$$
SQ_rh=e_0\otimes y_r,
\qquad Q_rf=e_{d-1}\otimes f_r.
\tag{1.3}
$$
其中 $y_r=\alpha_r\mathsf N_r^*h_{d-1}$ 按形式理解，但 (1.3) 已保证其为原 Hilbert 向量。
由于 $y_0=0$，$SQ_rh$ 正是 $y$ 在正的 $2^r$ 倍数坐标上的投影；因此
$$
\|y_r\|\to0,
\qquad \|f_r\|\to0.
\tag{1.4}
$$
从这里起不再变换来源 $h,y,f$。

## 2. N 型：完整低 carry 与单个高 coherent 行

当 $i<r$，原准确权乘积给
$$
\mathsf N_i^*Q_rh
=\alpha_i^{-1}e_{2^i-1}\otimes y_r.
\tag{2.1}
$$
当 $i\ge r$ 时，$\mathsf N_i^*$ 保留每个低头坐标，因此没有跨越 $Q_r$ 的项。
令
$$
v_r^{N}=\sum_{i=0}^{r-1}\frac{a_i}{\alpha_i}e_{2^i-1},
\qquad
\lambda_r^{N}=\|v_r^N\|
=\left[\sum_{i=0}^{r-1}\frac{a_i^2}{\alpha_i^2}\right]^{1/2}.
\tag{2.2}
$$
则全部低头误差准确为 $-v_r^N\otimes y_r$。

由非全满低头向全满低头的 N 型跃迁没有 borrow：它只能从低头恰缺位 $i$ 的行创建该位。因此定义
$$
\mathcal H_r^N(h)
=\sum_{i=0}^{r-1}a_i h_{d-1-2^i},
\tag{2.3}
$$
便有
$$
Q_rT_N^*h^{<r}=e_{d-1}\otimes\mathcal H_r^N(h).
$$
两个误差分别位于低头非顶行与顶行，严格正交。故
$$
\boxed{
\|T_N^*h^{<r}-f\|^2
=(\lambda_r^N)^2\|y_r\|^2
 +\|\mathcal H_r^N(h)-f_r\|^2.
}
\tag{2.4}
$$
连同输入图分量，得到
$$
\boxed{
\|Sh^{<r}-y\|^2+\|T_N^*h^{<r}-f\|^2
=[1+(\lambda_r^N)^2]\|y_r\|^2
 +\|\mathcal H_r^N(h)-f_r\|^2.
}
\tag{2.5}
$$
所有低位 carry 已在 (2.1)--(2.2) 中完整保留；高行 (2.3) 是原同一个 $h$ 的 coherent 行。

## 3. Y 型：按整低头周期重组全部真实逆

对 $0\le i<r$ 置
$$
L_{ri}=2^{r-i},
\qquad \kappa_{ri}=\frac{d_r}{d_i^{L_{ri}}},
\qquad Z_{ri}=(I-\kappa_{ri}\mathsf N_r^*)^{-1}.
\tag{3.1}
$$
这里 $L_{ri}$ 是正偶数，准确有
$$
(\mathsf N_i^*)^{L_{ri}}=\kappa_{ri}\mathsf N_r^*.
$$
由 $d_r=\eta_{r-1}d_{r-1}^2$ 和
$d_{r-1}\le d_i^{L_{ri}/2}$，得
$$
0<\kappa_{ri}\le\eta_{r-1}<1/2,
\qquad \|Z_{ri}\|\le2,
\qquad \|Z_{ri}-I\|\le2\eta_{r-1}.
\tag{3.2}
$$
所有 $Z_{ri}$ 是同一个原真实高尾上的有界逆，没有换用纯尾。

原范数收敛的 Cayley 级数按模 $L_{ri}$ 重组为
$$
\mathsf Y_i^*
=\left[
\sum_{k=1}^{L_{ri}-1}(-1)^{k-1}(\mathsf N_i^*)^k
-\kappa_{ri}\mathsf N_r^*
\right]Z_{ri}.
\tag{3.3}
$$
最后一项保留低头坐标，因而在两个跨顶行边界中都不出现。

记 $W_j=\prod_{\nu=1}^j\alpha_{v_2(\nu)}$、$W_0=1$。定义准确有限头向量和行
$$
\ell_{ri}
=\sum_{k=1}^{L_{ri}-1}
(-1)^{k-1}\frac{W_{k2^i-1}}{d_i^k}e_{k2^i-1},
\tag{3.4}
$$
$$
\mathfrak h_{ri}(h)
=\sum_{k=1}^{L_{ri}-1}
(-1)^{k-1}\frac{W_{k2^i}}{d_i^k}
h_{d-1-k2^i}.
\tag{3.5}
$$
于是整个真实低、高跨界算子分别是
$$
\mathcal L_r^Y y_r
=\sum_{i=0}^{r-1}a_i\,\ell_{ri}\otimes Z_{ri}y_r,
$$
$$
\mathcal H_r^Y(h)
=\sum_{i=0}^{r-1}a_i Z_{ri}\mathfrak h_{ri}(h).
\tag{3.6}
$$
有限头向量 $\ell_{ri}$ 可能相互重叠，(3.6) 使用其完整 Gram，不能把 $i$ 项的平方范数相加。

核对系数：从低头顶行加 $p=k2^i<d$，权乘积为
$\alpha_rW_{p-1}$，留下一个真实高尾 $\mathsf N_r^*$；将它和 $\alpha_r$ 合为 (1.3) 的 $y_r$，就得到 (3.4)。从低头 $d-1-p$ 加到顶行的权乘积为 $W_p$，给出 (3.5)。额外每绕过一个低头周期恰乘 $\kappa_{ri}\mathsf N_r^*$，其全部次数由 (3.3) 的同一个 $Z_{ri}$ 支付。

由此得到 Y 型的准确两正交项：
$$
\boxed{
\|T_Y^*h^{<r}-f\|^2
=\|\mathcal L_r^Y y_r\|^2
 +\|\mathcal H_r^Y(h)-f_r\|^2.
}
\tag{3.7}
$$
输入图误差仍准确为 $\|y_r\|^2$。

## 4. Y 型全部高尾逆相对真实有限头的误差已付

令 $T_Y^{[r]}$ 为原低 $r$ 位真实有限头，保留其全部低位 carry。定义
$$
v_r^Y=\sum_{i=0}^{r-1}a_i\ell_{ri},
\qquad \lambda_r^Y=\|v_r^Y\|,
$$
$$
\mathcal H_r^{Y,[r]}(h)
=\sum_{i=0}^{r-1}a_i\mathfrak h_{ri}(h).
\tag{4.1}
$$
后者正是 $(T_Y^{[r]})^*$ 的顶行作用在 $h^{<r}$；没有取平坦头。

有限头原逆界给
$$
\|\ell_{ri}\|\le3/\alpha_i,
\qquad \|\mathfrak h_{ri}\|\le3.
\tag{4.2}
$$
第一式也可由
$\ell_{ri}=\alpha_i^{-1}(I-Q_r)(I+(\mathsf N_i^{[r]})^*)^{-1}e_{2^i-1}$
直接核对；第二式是有限头 $\mathsf Y_i^*$ 顶行的压缩范数。
结合 (1.2)、(3.2) 和 $\sum_i a_i<2$，得到
$$
\boxed{
\|\mathcal L_r^Y y_r-v_r^Y\otimes y_r\|
\le12\frac{\alpha_r}{\alpha_{r-1}^2}\|y\|,
}
\tag{4.3}
$$
$$
\boxed{
\|\mathcal H_r^Y(h)-\mathcal H_r^{Y,[r]}(h)\|
\le12\frac{\alpha_r}{\alpha_{r-1}^2}\|y\|.
}
\tag{4.4}
$$
这两项都已作用在同一个最大图来源上。尤其 (4.4) 没有先假定可能发散的 $\|h^{<r}\|$ 一致有界，而是显式付了 (1.2) 的 $\alpha_{r-1}^{-1}$。

原 $L_j=-\log\alpha_j$ 给
$$
L_{j+1}-2L_j
=\frac{3920}{3}16^j-540\,8^j+\frac{850}{3}
\ge\frac{2300}{3}16^j.
$$
故两项均至多
$$
\boxed{12e^{-760\,16^{r-1}}\|y\|.}
\tag{4.5}
$$
这完成了所有 $Z_{ri}$ 的真实源费用；没有将固定 $r$ 逐逆收敛当成移动来源的一致结论。

## 5. 这条明确前缀截断的准确判据

为统一记号，N 型取
$\mathcal H_r^{N,[r]}=\mathcal H_r^N$。
由 (1.4)、(2.5)、(3.7) 和 (4.3)--(4.5)，对任一模型，有
$$
(Sh^{<r},T_\bullet^*h^{<r})\longrightarrow(y,f)
$$
当且仅当同一来源的两笔有限头边界费用满足
$$
\boxed{
\lambda_r^\bullet\|y_r\|\longrightarrow0,
\qquad
\|\mathcal H_r^{\bullet,[r]}(h)\|\longrightarrow0.
}
\tag{5.1}
$$
N 型没有 (4.5) 误差；Y 型的误差已统一趋零。

因此 (5.1) 为此前 $G_0^*$ 图核心中的完整实际输入提供了一个可单独核验的充分预算。若它对某个给定最大图源成立，则这些 $h^{<r}\in\mathcal H$ 给真正的图逼近，随后可在每个 $h^{<r}$ 上作普通有限支撑逼近。
本稿只证明这条指定截断的“当且仅当”，未证明所有图可逼近的源都必须满足 (5.1)，也没有证明一般真正 $W$ 的规范原像已经属于最大图域。

两笔费用涉及同一个 $h$ 的低头全占缺位行与同一个 $Sh$ 的低零头尾；没有将整个总孔层、有限 $C$ 的近核或不同来源替换进来。第二道精确可除值域核心及 $N=M$ 继续开放。
