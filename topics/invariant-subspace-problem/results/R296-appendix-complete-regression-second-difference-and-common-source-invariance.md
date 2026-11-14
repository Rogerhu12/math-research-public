# 任意出生桥创新的完整回归系数二阶差

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；出生二线性拟合形式由 boundary_core 独立提出，本文核实并推广到任意出生。

**状态：以下恒等式已证明；统一能量上界尚未由它推出。** 本文是[全出生残差与真实桥稿](R296-all-birth-residual-regression-two-band-lift-and-physical-innovation.md)的完整补充。所有投影、切片范数及物理源约定沿用该稿。

## 1. 每个高度的唯一完整拟合系数

固定任意正权 \(b_i\)、\(z_i=b_i^2\)，取 \(s\ge1\)、\(h=M-2s\ge1\)、\(f\in K_s\)。令
\[
\Phi=\Phi_{s,f},\qquad
q_j=\Pi_{\le s-1}^{(j)}\Phi,
\qquad s\le j\le M-s+1.
\tag{1.1}
\]
右侧是切片函数；下文总把 \(q_j\) 取为其唯一齐次 \((s-1)\) 次多线性代表。其唯一性来自该范围中 \((s-1)\) 次包含特征的满列秩；常数和更低次特征已由固定基数恒等式吸收，绝非被删去。

于是有唯一完整物理系数 \(g_j(f)\in\mathcal H_{s-1}\) 使
\[
q_j=\Phi_{s-1,g_j(f)}.
\tag{1.2}
\]
这些系数一般不在低一出生 primitive 空间 \(L=K_{s-1}\)。记 \(F_m^{(r)}=d^m(d^*)^m/(m!)^2|_{\mathcal H_r}\)。主稿的完整正规方程给出
\[
\boxed{
g_{s+m}(f)=\frac1{m+1}
\left(F_{m+1}^{(s-1)}\right)^{-1}dF_m^{(s)}f,
\qquad 0\le m\le h+1.
}
\tag{1.3}
\]
所用低出生完整逆始终存在。最高端 \(m=h+1\) 的上出生 \(F_m^{(s)}\) 可以奇异，但本式没有取它的逆；它仍是完整低阶正规方程的准确解。尤其 \(g_s=0\)。

令 \(\Pi_{\le s-2}^{(j)}=0\) 当 \(s=1\)，否则取真实 \(\mu_j\) 权投影。

## 2. 同一个共同映射的系数形式

固定 \(1\le n\le h\)，置 \(k=s+n\)。主稿的共同映射
\[
\mathsf Z_n=\frac1{n+1}
\left(\mathsf U_k\mathcal R_{k,s}
+\mathcal R_{k+1,s-1}\Theta_{n-1}\right),
\qquad \Theta_{n-1}=L_{n+1}BC_{n-1},
\]
有以下完全系数化的表示：
\[
\boxed{
\mathsf Z_nf
=(I-\Pi_{\le s-2}^{(k+1)})
\left(\Phi-2q_k+q_{k-1}\right).
}
\tag{2.1}
\]
所有多项式都在同一个 \((k+1)\) 元切片上评价。

证明。因为 \(\mathcal R_{j,s}f=\Phi-q_j\)，而升层 \(\mathsf U\) 分别在最高 \(s\) 次和齐次 \(s-1\) 次项上乘以相应的补数，故在 \(k\) 元切片上
\[
\mathcal R_{k,s-1}\Theta_{n-1}f
=(n+1)q_{k-1}-nq_k.
\tag{2.2}
\]
把这个相同低出生源运输到 \(k+1\) 元切片，恰是将右侧按新切片重新投掉全部 \(\le s-2\) 次项：
\[
\mathcal R_{k+1,s-1}\Theta_{n-1}f
=(I-\Pi_{\le s-2}^{(k+1)})
\bigl((n+1)q_{k-1}-nq_k\bigr).
\tag{2.3}
\]
这里无需把原拟合系数误当成 primitive；两代表之差属于 \(\operatorname{Ran}d^*\)，在每个新切片上仍仅给 \(\le s-2\) 次项。

又
\[
\mathsf U_k\mathcal R_{k,s}f=(n+1)\Phi-(n+2)q_k,
\]
它已经正交于全部 \(\le s-2\) 次特征。将这两式代回定义、合并齐次系数，即得 (2.1)。

## 3. 真实创新是拟合系数的二阶差，符号必须保留

主稿还证明
\[
\mathsf Z_n=\mathcal R_{k+1,s}
-\mathcal R_{k+1,s-1}\delta_{n+1}^*,
\quad
\delta_{n+1}^*=
\frac{L_{n+2}BC_n-L_{n+1}BC_{n-1}}{n+1}.
\]
结合 (2.1)，得到
\[
\boxed{
(I-\Pi_{\le s-2}^{(k+1)})
\left(q_{k+1}-2q_k+q_{k-1}\right)
=-\mathcal R_{k+1,s-1}\delta_{n+1}^*f.
}
\tag{3.1}
\]
也就是说，二阶差的最高低出生残差对应的是 \(-\delta_{n+1}^*\)，不是正号。它的平方能量当然不受这个符号影响。

令 \(P_L\) 为原物理 \(\mathcal H_{s-1}\) 到 \(L\) 的正交投影。由残差源同构，(3.1) 等价于
\[
\boxed{
P_L\bigl(g_{k+1}-2g_k+g_{k-1}\bigr)
=-\delta_{n+1}^*.
}
\tag{3.2}
\]
特别，真实创新还有一个仅使用完整层逆的表达：
\[
\begin{aligned}
\delta_{n+1}^*=-P_L\Bigg[&
\frac1{n+2}\left(F_{n+2}^{(s-1)}\right)^{-1}dF_{n+1}^{(s)}\\
&-\frac2{n+1}\left(F_{n+1}^{(s-1)}\right)^{-1}dF_n^{(s)}
+\frac1n\left(F_n^{(s-1)}\right)^{-1}dF_{n-1}^{(s)}
\Bigg]\bigg|_{K_s}.
\end{aligned}
\tag{3.3}
\]
只有在所有完整拟合系数构造完成之后，才作 \(P_L\)；把各完整逆提前压缩到 primitive 子空间会改变问题。

精确创新费用为
\[
\boxed{
\left\|(I-\Pi_{\le s-2}^{(k+1)})
(q_{k+1}-2q_k+q_{k-1})\right\|_{k+1}^2
=\langle\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*f,f\rangle.
}
\tag{3.4}
\]

### 3.1 首边的完整系数核对

\(n=1\) 时，\(g_s=0\)、\(dF_1f=-2Bf\)，所以
\[
g_{s+1}=-\left(F_2^{(s-1)}\right)^{-1}Bf.
\]
由既有 R288 三塔完整 \(F_3\) Schur 式，
\[
P_Lg_{s+2}=-\tfrac12(L_3BC_1+3L_2B)f,
\qquad P_Lg_{s+1}=-L_2Bf.
\]
故二阶差确为 \(-\tfrac12(L_3BC_1-L_2B)f=-\Delta^*f\)。这里低二出生的完整拟合分量仍存在；只是最后的低一出生残差投影将它剔除，不能在求解拟合时提前剔除。

## 4. 商代表改变不影响二阶差

若将最高次物理代表换成 \(f+d^*u\)，\(u\in\mathcal H_{s-1}\)，则在第 \(j\) 个切片上
\[
\Phi_{s,f+d^*u}=\Phi_{s,f}+(j-s+1)\Phi_{s-1,u}.
\]
所以完整拟合系数准确变为
\[
g_j\longmapsto g_j+(j-s+1)u.
\tag{4.1}
\]
三个相邻高度的二阶差严格不变。式 (2.1) 的整个共同映射也不变，因为在 \(k+1\) 切片上新增系数为
\((n+2)-2(n+1)+n=0\)。这使最大原子或其他商坐标约化可以先选择同一个便利代表，然后在三个高度共同使用；不能在各高度分别选择不同的商代表而不补运输项。

## 5. 出生二的准确线性特例

取 \(s=2\)，写最高次特征
\(\Phi(x)=\sum_{i<j}a_{ij}x_ix_j\)。记其在 \(\mu_j\) 下对全部线性特征的最优拟合为 \(q_j=t_j\cdot x\)。常数已由 \(\sum_i x_i=j\) 吸收在该唯一线性代表里。

于是 (2.1) 变成
\[
\boxed{
\mathsf Z_nf=
\operatorname{center}_{\mu_{k+1}}
\bigl[\Phi-(2t_k-t_{k-1})\cdot x\bigr],
\qquad k=n+2.
}
\tag{5.1}
\]
创新低出生残差是
\[
\operatorname{center}_{\mu_{k+1}}
\bigl[(t_{k+1}-2t_k+t_{k-1})\cdot x\bigr]
=-\mathcal R_{k+1,1}\delta_{n+1}^*f.
\tag{5.2}
\]
\(a_{ij}\mapsto a_{ij}+u_i+u_j\) 使 \(t_j\mapsto t_j+(j-1)u\)，因此二阶差原样保留。这正是出生二最大原子交换坐标可以接入的共同线性回归差；它仍需要在真实源精度很小的方向支付 (5.1) 的能量。

本文给的是接口和恒等式，没有从固定高度残差的正性或夹逼推断相邻共同映射具有统一范数。
