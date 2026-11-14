# R295：出生一真实 Turán 余量测度与全部高度加强 S1

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core；概率余量与原连续尾应用由 root 共同推导。

**状态：以下恒等式与参数相关的加强 S1 已证明。** 对任意有限正权行，所付常数是准确的相邻分配函数比值 $\rho_k=e_k^2/(e_{k-1}e_{k+1})$；它在任意正权行上没有统一上界。对原连续平方权 $z_j=j^{-4}$，本文另付统一常数 $674/81$，覆盖整个真实出生一及全部合法高度。没有外推到其他出生或原 graph $\Gamma$。

输入是 [R288 完整一孔精度](R288-appendix-birth-one-precision-coefficients-and-common-source-s2-congruences.md)、[R293 加强缺陷的准确归一](R293-appendix-all-height-strengthened-s1-heavy-bit-equivalence.md)和 [R294 固定高度无限行极限](R294-birth-one-uniform-diagonal-gram-comparison-and-common-newton-blocks.md)。本文的分拆恒等式不需要外部协方差夹逼定理；无限段只使用 R294 中完整 $F_j$ 的可逆性及固定高度范数极限，不使用其外部协方差下界。

## 1. 共同物理源与实际二阶均值差

取 $M\ge3$ 个正权 $b_i$，写
$$
z_i=b_i^2,\quad S=\sum_i z_i,\quad
B_0=\operatorname{diag}(b_i),\quad T=\operatorname{diag}(z_i),\quad
K=b^\perp,\quad P=P_K.
$$
$B_0$ 是对角坐标变换，不是 R293 的三次桥。以下 $e_j=e_j(z)$，删去第 $i$ 位的对称和记为 $e_j^i$。

对 $0\le n\le M-2$，使用实际完整一孔矩阵及其最小逆 Gram
$$
F_n=\frac{d^n(d^*)^n}{(n!)^2}\bigg|_{\mathcal H_1},\qquad
\Gamma_n=P F_n^{-1}|_K,\qquad C_n=\Gamma_n^{-1}.
\tag{1.1}
$$
始终先求完整逆，再压到同一个 $K$。最高端 $C_{M-1}=0$ 只表示真实下一精度为零，不引入不存在的 $\Gamma_{M-1}$。

令
$$
u_n=(b_i e_n^i)_i,\qquad \eta_n=Pu_n,\qquad r=PTb.
$$
已有完整 Schur 身份的零延拓形式为
$$
\widetilde C_n=F_n-\frac{u_nu_n^*}{e_{n+1}},\qquad
\widetilde C_n b=0,\qquad \widetilde C_n|_K=C_n.
\tag{1.2}
$$
按实际条目直接计数得
$$
F_nTb=S u_n-(n+1)u_{n+1},\qquad
u_n^*Tb=S e_{n+1}-(n+2)e_{n+2}.
$$
代入 (1.2) 后 $S u_n$ 消去，得到
$$
\boxed{C_nr=(n+2)\frac{e_{n+2}}{e_{n+1}}\eta_n-(n+1)\eta_{n+1}.}
\tag{1.3}
$$
右边也可直接使用 $u$ 替代 $\eta$，因为其与 $b$ 的配对已经为零。

出生零的实际 $j$ 级 Gram 是 $L_j=1/e_j$；三次桥的伴随作用在真空上恰为 $r$。故 R293 的加强创新在 $1\le n\le M-2$ 是
$$
\delta_{n+1}=\frac1{n+1}\left(\frac{C_nr}{e_{n+2}}-\frac{C_{n-1}r}{e_{n+1}}\right)
=\frac{2u_n}{e_{n+1}}-\frac{u_{n+1}}{e_{n+2}}-\frac{u_{n-1}}{e_n}.
\tag{1.4}
$$

现在令 $\mu_k$ 为大小 $k$ 的实际外场子集分布，
$$
\mu_k(I)=z_I/e_k,\qquad p_k=\mathbb E_{\mu_k}\mathbf1_I,\qquad
\Sigma_k=\operatorname{Cov}_{\mu_k}(\mathbf1_I).
$$
约定 $p_0=0,p_M=\mathbf1,\Sigma_0=\Sigma_M=0$。因为
$(p_k)_i=z_i e_{k-1}^i/e_k$，取 $k=n+1$ 后 (1.4) 准确变成
$$
\boxed{B_0\delta_{n+1}=q_k:=2p_k-p_{k-1}-p_{k+1}.}
\tag{1.5}
$$
这里 $\mathbf1^*q_k=0$，所以 $B_0^{-1}q_k\in K$；没有省略任何物理投影。

## 2. 加强 S1 的准确概率矩阵形式

有限维完整 Schur 身份及其真实逆给
$$
\widetilde C_n=e_k B_0^{-1}\Sigma_kB_0^{-1},\qquad
\widetilde\Gamma_{n-1}=rac1{e_{k-1}}PB_0\Sigma_{k-1}^{\dagger}B_0P.
\tag{2.1}
$$
$2\le k\le M-1$ 时 $\Sigma_{k-1}$ 在 $\mathbf1^\perp$ 上严格正定。相乘时，由各 $\Sigma_j\mathbf1=0$，夹在两侧的 $P$ 全部准确消去，因而
$$
\widetilde C_n\widetilde\Gamma_{n-1}\widetilde C_n
=\frac{e_k^2}{e_{k-1}}B_0^{-1}
\Sigma_k\Sigma_{k-1}^{\dagger}\Sigma_kB_0^{-1}.
\tag{2.2}
$$
设
$$
\rho=\rho_k=\frac{e_k^2}{e_{k-1}e_{k+1}}>1.
$$
R293 的实际加强缺陷
$$
E_n^{(\kappa)}=\kappa C_n\Gamma_{n-1}C_n-C_{n+1}
-e_{k+1}\delta_{n+1}\delta_{n+1}^*
$$
因此满足准确同余
$$
\boxed{\widetilde E_n^{(\kappa)}
=e_{k+1}B_0^{-1}\mathcal D_k^{(\kappa)}B_0^{-1},}
\qquad
\boxed{\mathcal D_k^{(\kappa)}
=\kappa\rho\Sigma_k\Sigma_{k-1}^{\dagger}\Sigma_k
-\Sigma_{k+1}-q_kq_k^*.}
\tag{2.3}
$$
全部概率矩阵的共同核含 $\mathbf1$。在物理侧共同核为 $b$。于是 $E_n^{(\kappa)}\succeq0$ 与 $\mathcal D_k^{(\kappa)}\succeq0$ 等价。$k=M-1$ 时使用真实 $\Sigma_M=0$，所以最高硬端也在此公式中。

## 3. 同一个占据和的准确分拆测度

分别取独立对子
$$
(I,J)\sim\mu_k\otimes\mu_k,\qquad
(I_-,I_+)\sim\mu_{k-1}\otimes\mu_{k+1}.
$$
两种对子都考察占据和 $Y=\mathbf1_I+\mathbf1_J$。固定交集 $A$ 与对称差 $D$，其中
$$
|A|=k-r,\qquad |D|=2r,\qquad A\cap D=\varnothing.
$$
同一个 $Y=2\mathbf1_A+\mathbf1_D$ 的单项权为 $z_A^2z_D$。
等秩对子有 $\binom{2r}{r}$ 个有序分拆；邻秩对子有 $\binom{2r}{r-1}$ 个，其中 $r=0$ 时后者为零。因此其非归一测度之差有非负系数
$$
\binom{2r}{r}-\binom{2r}{r-1}
=\frac1{r+1}\binom{2r}{r}=\operatorname{Cat}_r.
$$
该差测度的总质量为
$$
\Delta_k=e_k^2-e_{k-1}e_{k+1}
=\sum_{r=0}^{\min(k,M-k)}\operatorname{Cat}_r
\sum_{\substack{|A|=k-r,\ |D|=2r\\A\cap D=\varnothing}}z_A^2z_D>0.
\tag{3.1}
$$
它也就是二列矩形 Schur 多项式 $s_{(2^k)}$。下文只使用显示的非负分拆计数。

令 $\nu_R$ 为 (3.1) 归一化后的占据和分布，记其均值 $p_R$、协方差 $\Sigma_R$。如果 $\mathcal P$、$\mathcal Q$ 分别是上面两种独立子集对的占据和分布，则有准确的概率测度身份
$$
\boxed{\mathcal P=\rho^{-1}\mathcal Q+(1-\rho^{-1})\nu_R.}
\tag{3.2}
$$
这不是只比较某个标量方差，而是保留全部共同坐标的测度混合。

两种独立对子给
$$
\mathbb E_{\mathcal P}Y=2p_k,\quad
\operatorname{Cov}_{\mathcal P}Y=2\Sigma_k,
$$
$$
\mathbb E_{\mathcal Q}Y=p_{k-1}+p_{k+1}=2p_k-q_k,\quad
\operatorname{Cov}_{\mathcal Q}Y=\Sigma_{k-1}+\Sigma_{k+1}.
$$
先比较均值，再使用混合分布的完整协方差公式，得到
$$
p_R=2p_k+\frac{q_k}{\rho-1},
$$
$$
\boxed{2\rho\Sigma_k
=\Sigma_{k-1}+\Sigma_{k+1}
+(\rho-1)\Sigma_R+\frac{\rho}{\rho-1}q_kq_k^*.}
\tag{3.3}
$$
所有协方差都来自同一实际权行；$\Sigma_R$ 也可由
$\nabla_{\log z}^2\log\Delta_k$ 得到。本文没有把它替换成任取的正矩阵。

## 4. 全部高度的参数相关加强 S1 与准确剩余

简写 $A=\Sigma_{k-1}$、$B=\Sigma_k$、$C=\Sigma_{k+1}$、$q=q_k$。这些矩阵都在共同的 $\mathbf1^\perp$ 上使用；其中 $A>0$。将 (3.3) 代入 (2.3)，取 $\kappa=\rho$，得到一个完整平方分解
$$
\boxed{
\mathcal D_k^{(\rho)}
=(\rho B-A)A^{\dagger}(\rho B-A)
+(\rho-1)\Sigma_R+\frac{qq^*}{\rho-1}\succeq0.
}
\tag{4.1}
$$
因此对任意正权有限行、出生一和全部 $1\le n\le M-2$，
$$
\boxed{E_n^{(\rho_{n+1})}\succeq0.}
\tag{4.2}
$$
有限正权行中 (4.1) 在 $\mathbf1^\perp$ 上实际上严格正定：余量测度的 $r=0$ 部分给所有 $k$ 元子集的 $2\mathbf1_I$ 正质量，其共同仿射包恰为总占据数 $2k$ 的超平面，故 $\Sigma_R$ 在 $\mathbf1^\perp$ 上正定。这里包含实际三次桥创新，而非仅有普通相邻 Gram 序。在具有下一合法 Gram 的内部高度，进一步得到
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
\preceq\rho_{n+1}\Gamma_{n-1}.
\tag{4.3}
$$

同一个身份也准确标出常数一仍需支付的部分：
$$
\boxed{
\mathcal D_k^{(1)}
=\rho(B-A)A^{\dagger}(B-A)
+(\rho-1)(\Sigma_R-A)+\frac{qq^*}{\rho-1}.
}
\tag{4.4}
$$
不能把第二项免费当成非负。例如 $M=4,k=2,z=(t,t,1,1)$，取 $v=(1,-1,0,0)$，则
$$
v^*\Sigma_1v=\frac{t}{t+1},\qquad
v^*\Sigma_Rv=
\frac{4t(t^2+6t+1)}{t^4+4t^3+10t^2+4t+1}.
$$
前者趋一，后者趋零。这个例子只排除 $\Sigma_R\succeq A$ 的独立强化，不否定完整 (4.4) 的正性。

由 (3.3) 还立即得到创新自身的真实能量预算
$$
q_kq_k^*\preceq2(\rho_k-1)\Sigma_k,
\qquad
q_k^*\Sigma_k^{\dagger}q_k\le2(\rho_k-1),
\tag{4.5}
$$
以及物理形式
$$
\boxed{e_{k+1}\delta_{n+1}\delta_{n+1}^*
\preceq2\left(\frac{e_k}{e_{k-1}}-\frac{e_{k+1}}{e_k}\right)C_n.}
\tag{4.6}
$$
(4.6) 不能单独替代 (2.3) 中的混合逆项；它只是 (3.3) 所支付的一条实际秩一预算。

## 5. 从最大子集原子到统一常数

对独立 $I,J\sim\mu_k$，置 $r=|I\setminus J|$。在第3节相同的分拆中，邻秩计数与等秩计数的比为 $r/(r+1)$，所以
$$
\boxed{\rho_k^{-1}=\mathbb E\frac{r}{r+1}.}
\tag{5.1}
$$
由于 $r\ge1$ 时 $r/(r+1)\ge1/2$，
$$
\rho_k^{-1}\ge\frac12\mathbb P(I\ne J)
=\frac12\left(1-\sum_I\mu_k(I)^2\right)
\ge\frac12(1-p_{\max,k}),
\tag{5.2}
$$
其中 $p_{\max,k}=\max_I\mu_k(I)$。特别地，只要最大权子集之外还有一个权重至少为其 $\theta$ 倍的子集，就有
$$
p_{\max,k}\le\frac1{1+\theta},\qquad
\boxed{\rho_k\le\frac{2(1+\theta)}{\theta}.}
\tag{5.3}
$$
任意正权行上 $\rho_k$ 确可无界：仍取 $M=4,k=2,z=(t,t,1,1)$，则 $\rho_k\sim t/4$。因此 (4.2) 的一般结论是参数相关的，不是任意独立权的普适有限常数定理。

## 6. 原连续尾的统一加强 S1

取原连续平方权
$$
z_j=j^{-4},\qquad j=x,x+1,\ldots,\qquad x=m+1\ge2.
$$
先在任意连续有限头内工作。对 $2\le k\le M-1$，最大权 $k$ 元子集是
$I_0=\{x,\ldots,x+k-1\}$。将末位换成下一位 $x+k$，得到另一个合法子集，权重比为
$$
\theta=\left(\frac{x+k-1}{x+k}\right)^4\ge\left(\frac34\right)^4=\frac{81}{256}.
$$
于是 (5.3) 给与尾头 $m$、截断长度 $M$ 和合法高度均无关的界
$$
\boxed{\rho_k\le\frac{674}{81}.}
\tag{6.1}
$$
由 $C_n\Gamma_{n-1}C_n\succeq0$，(4.2) 对更大的常数仍成立。因此所有这些真实有限头、出生一和全部合法高度满足
$$
\boxed{E_n^{(674/81)}\succeq0.}
\tag{6.2}
$$

对无限原连续尾，固定任意有限 $n$，先将首 $N$ 位的权行以零延拓放入共同 $\ell^2$，其共同源为 $K^{(N)}=(b^{(N)})^\perp$。头内使用 (6.2)；头外每个单孔坐标的实际 $\Gamma_j=(e_j(z_{\le N}))^{-1}I$，三次桥和创新均为零，故加强缺陷尾块是 $\kappa e_n^2/e_{n-1}-e_{n+1}\ge0$，由 $\kappa\ge1$ 及初等对称和的标量 Newton 式支付。因此有限头正性先延拓到整个 $K^{(N)}$，没有省略尾直和。再令 $N\to\infty$；$e_j$ 收敛，完整 $F_j$、真实 $\Gamma_j$ 及其精度在 R294 已付的共同空间表示下作算子范数收敛；$r=PTb$ 与 (1.4) 的创新也收敛。有限头 (6.2) 因而直接在物理 $K$ 上传到无限行：
$$
\boxed{E_n^{(674/81)}\succeq0\qquad(n\ge1).}
\tag{6.3}
$$
每个固定高度都合法，且常数相同；不需要随高度增长的截断速率。证明没有把无限 $B_0^{-1}$ 或 $\Sigma_{k-1}^{\dagger}$ 误作有界算子：无限结论通过真实有界物理矩阵的有限头极限取得。

删去正桥项并作 $\Gamma_n$ 同余，进一步得到原连续尾整个出生一的真正全高度算子相邻序
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
\preceq\frac{674}{81}\Gamma_{n-1}\qquad(n\ge1).}
\tag{6.4}
$$
这已控制实际 $\Gamma_n$ 的中间方向，而不只是 R294 的共同对角代理或逐向量标量式。原其他出生、共同 graph 源的跨出生逆传播、以及不变子空间问题的完成标准仍不由此结论推出。


## 后续范围更新

[统一常数附录](R295-appendix-universal-birth-one-strengthened-s1-by-atomic-splitting.md)已以最大原子分区及真实加权扰动证明任意有限正权、整个出生一、全部高度的加强 S1 可取统一常数1024；无限正ℓ²行也有非严格结论。本文的原连续尾较小常数674/81继续有效，一般出生与graph仍须另证。
