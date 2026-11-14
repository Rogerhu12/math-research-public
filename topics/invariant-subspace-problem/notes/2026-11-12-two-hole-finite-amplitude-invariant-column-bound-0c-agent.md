# 两孔测试在任意不变子空间内的有限幅实现

日期：2026-11-12。作者：l2_moments。R167 的独立后续笔记，暂不占结果号。
状态：完整定量必要条件；没有从柱投影上界推出未知不变子空间为零。

## 1. 范围和主结论

沿用 R167 的
$$
W=\sum_i b_iY_i,\qquad Z=\sum_i b_i^2K_i,\qquad
Y_i=N_i(I+N_i)^{-1},\quad K_i=N_i(I+N_i)^{-2}.
$$
固定 $b\in\ell^1$，并设 $b_i=(i+1)^{-2}$ 最终成立。
令 $\mathcal M\ne0$ 为闭 $A$-不变子空间。
假设存在 $Q\in B(\mathcal M)$ 使
$$
Z|_{\mathcal M}=W|_{\mathcal M}\,Q.
\tag{1.1}
$$
这里 $W,Z\in\mathcal A$，故均保持 $\mathcal M$。
$W|_{\mathcal M}$ 单射，且 $WZ=ZW$；因此
$$
QW|_{\mathcal M}=W|_{\mathcal M}Q,
$$
进而
$$
\|Zx\|\le\|Q\|\,\|Wx\|\qquad(x\in\mathcal M).
\tag{1.2}
$$

记 $\Pi_{0,L}$ 为低 $L$ 位物理模式全为0的正交投影。
则对每个 $\gamma<260/3$，存在与 $j,L$ 无关的常数，使充分大的 $j$ 和 $L>j+1$ 满足
$$
\boxed{
\|\Pi_{0,L}|_{\mathcal M}\|
\le C_{b,Q,\gamma}\,j^5
\left(e^{-\gamma16^j}+\sum_{i\ge L}|b_i|\right).
}
\tag{1.3}
$$
特别，在当前慢尾下，
$$
\boxed{
\|\Pi_{0,L}|_{\mathcal M}\|
\le C_{b,Q}\,
\frac{(1+\log\log(L+3))^5}{L}
}
\tag{1.4}
$$
当 $L$ 足够大。

这是用真正保持 $\mathcal M$ 的多项式测试得到的统一算子范数必要条件。
它不需要给 $\mathcal M$ 中未知向量指定尾部收敛速度。
但 (1.4) 仍是上界；全本质支撑只给每个固定 $L$ 时该范数为正，不能与之构成矛盾。

## 2. 实际有限幅多项式

置 $k=j+1$，定义
$$
F_{j,L}=\prod_{\substack{0\le i<L\\i\ne j,k}}N_i,
$$
$$
P_{j,L}=
F_{j,L}\big[
b_jN_j(I-N_k)-b_k(I-N_j)N_k
\big].
\tag{2.1}
$$
每个 $P_{j,L}$ 都是真正的 $A$ 多项式，所以保持 $\mathcal M$。
由于 $\|N_i\|=1$，
$$
\boxed{\|P_{j,L}\|\le2(|b_j|+|b_k|).}
\tag{2.2}
$$
这与头长 $L$ 无关。

相应纯算子为
$$
F^0_{j,L}=\prod_{\substack{0\le i<L\\i\ne j,k}}E_i,
$$
$$
P^0_{j,L}=
F^0_{j,L}\big[
b_jE_j(I-E_k)-b_k(I-E_j)E_k
\big].
\tag{2.3}
$$
令
$$
W^0_{<L}=\sum_{i<L}b_iE_i,\qquad
Z^0_{<L}=\sum_{i<L}b_i^2E_i,\qquad
E_{<L}=\prod_{i<L}E_i.
$$
平方零且两两交换的 $E_i$ 给精确算子恒等式
$$
\boxed{
W^0_{<L}P^0_{j,L}=0,\qquad
Z^0_{<L}P^0_{j,L}
=\Delta_j E_{<L},
}
\tag{2.4}
$$
其中
$$
\Delta_j=b_jb_k(b_k-b_j).
\tag{2.5}
$$
这对任意输入成立，并没有先把输入替换为参考真空。

例如，在其余低位都已被 $F^0$ 填满之后，记输入两位 $(j,k)$ 的尾列为 $x_{00},x_{01},x_{10},x_{11}$。
(2.3) 的输出为
$$
b_jh_k\otimes x_{00}-b_kh_j\otimes x_{00}
+
e_L\otimes
\big[b_j(x_{01}-x_{00})-b_k(x_{10}-x_{00})\big].
\tag{2.6}
$$
最后的已填满头分量可以很大；它确实被 $W^0_{<L}$、$Z^0_{<L}$ 同时杀掉。
因此 (2.4) 不假设这些未知尾列相等，也不要求其差小。

## 3. 实际多项式与纯算子的统一比较

设 $A_j$ 是低 $j$ 位有限链、张量尾部恒等的截断，满足
$$
\|A-A_j\|=\alpha_j,\qquad
\|A_j\|\le\|A\|=\alpha_0<1.
$$
记 $n_j=2^j-1$。
有
$$
\prod_{i<j}N_i=\frac{A^{n_j}}{W_{n_j}},
\qquad
\prod_{i<j}E_i=\frac{A_j^{n_j}}{W_{n_j}}.
$$
故
$$
\left\|\prod_{i<j}N_i-\prod_{i<j}E_i\right\|
\le
\delta_j:=
\frac{n_j\alpha_0^{n_j-1}\alpha_j}{W_{n_j}}.
\tag{3.1}
$$
对较高连续块只需普通 telescoping：
$$
\left\|\prod_{i=k+1}^{L-1}N_i-\prod_{i=k+1}^{L-1}E_i\right\|
\le\sum_{i=k+1}^{L-1}\eta_i.
$$
因此
$$
\|F_{j,L}-F^0_{j,L}\|
\le\delta_j+\sum_{i\ge j+2}\eta_i.
\tag{3.2}
$$
把 (2.1) 的两个剩余局部因子分别替换，得到保守界
$$
\|P_{j,L}-P^0_{j,L}\|
\le
4(|b_j|+|b_k|)
\left(\delta_j+\eta_j+\sum_{i\ge j+2}\eta_i\right).
\tag{3.3}
$$
所有乘积范数及替换常数均与 $L$ 无关。

本模型实际权公式给
$$
-\log\alpha_j=\frac{280}{3}16^j+O(8^j+j2^j),
$$
$$
-\log W_{2^j-1}=\frac{100}{15}16^j+O(8^j+j2^j).
$$
因此
$$
-\log\delta_j=\frac{260}{3}16^j+O(8^j+j2^j).
\tag{3.4}
$$
同时
$$
-\log\eta_{j-1}=\frac{175}{2}16^j+O(8^j+j2^j),
$$
且 $\sum_{i\ge j}\eta_i\le2\eta_j$ 对大 $j$ 成立。
于是令
$$
\varepsilon_j=
\delta_j+\eta_{j-1}+\sum_{i\ge j}\eta_i,
$$
则对每个 $\gamma<260/3$，
$$
\boxed{\varepsilon_j\le C_\gamma e^{-\gamma16^j}.}
\tag{3.5}
$$
这里用的是完整权公式；粗估计 $\eta_{j-1}\le e^{-77016^{j-1}}$ 单独并不足以给 (3.5) 的接近 $260/3$ 常数。

## 4. 在两孔加填满头范围上的真实作用误差

令 $\mathcal H_{j,L}$ 为三个物理头模式 $h_j,h_k,e_L$ 张量任意尾向量的直和。
它包含 $\operatorname{Ran}P^0_{j,L}$。
R167 逐位递推对两个孔模式给的界，在填满头模式上更小：
$$
\|(N_i-E_i)e_L\otimes y\|
\le(\alpha_L/\alpha_i)\|y\|,\qquad
\|N_i^2e_L\otimes y\|
\le(\alpha_L/\alpha_i)\|y\|.
$$
由于三头模式正交，逐分量估计至多损失 $\sqrt3$。
故 R167 的 $4r_i$、$28r_i$ 可在整个 $\mathcal H_{j,L}$ 上用 $4\sqrt3\,r_i$、$28\sqrt3\,r_i$ 替代，其中 $r_i\le\eta_{j-1}$。
由 (2.2) 的同样纯界，
$$
\left\|
\left(\sum_{i<L}b_iY_i-W^0_{<L}\right)P^0_{j,L}
\right\|
\le C_b(|b_j|+|b_k|)\eta_{j-1},
$$
$$
\left\|
\left(\sum_{i<L}b_i^2K_i-Z^0_{<L}\right)P^0_{j,L}
\right\|
\le C_b(|b_j|+|b_k|)\eta_{j-1}.
\tag{4.1}
$$
这里 $\sum|b_i|$、$\sum|b_i|^2$ 只进入固定常数。

记 $\tau_L=\sum_{i\ge L}|b_i|$。
两尾的算子范数分别至多 $3\tau_L$ 与 $9\tau_L^2$。
将 (3.3)、(4.1) 和 (2.4) 合并，得到
$$
\boxed{
\|WP_{j,L}\|
\le C_b(|b_j|+|b_k|)(\varepsilon_j+\tau_L),
}
\tag{4.2}
$$
$$
\boxed{
\|ZP_{j,L}-\Delta_jE_{<L}\|
\le C_b(|b_j|+|b_k|)(\varepsilon_j+\tau_L^2).
}
\tag{4.3}
$$
这是全空间算子范数比较。没有把某个未知 $x$ 的尾误差藏入 $o(1)$。

## 5. 核内关系给柱投影上界

由 $P_{j,L}\mathcal M\subseteq\mathcal M$ 和 (1.2)，
$$
\|ZP_{j,L}x\|\le\|Q\|\,\|WP_{j,L}x\|
\qquad(x\in\mathcal M).
$$
故 (4.2)—(4.3) 给
$$
|\Delta_j|\,\|E_{<L}|_{\mathcal M}\|
\le
C_b(|b_j|+|b_k|)
\big[(1+\|Q\|)\varepsilon_j+\|Q\|\tau_L+\tau_L^2\big].
\tag{5.1}
$$
因 $E_{<L}$ 是从全0头到全1头的部分等距，
$$
\|E_{<L}x\|=\|\Pi_{0,L}x\|.
$$
又 $|b_j|+|b_k|\asymp j^{-2}$，
$|\Delta_j|\asymp j^{-7}$，
且 $\tau_L\asymp L^{-1}$，这证明 (1.3)。

取
$$
j=\left\lceil\log_{16}\!\left(\frac{2\log(L+3)}{\gamma}\right)\right\rceil
$$
并令 $L$ 足够大，则 $j+1<L$、
$e^{-\gamma16^j}\le(L+3)^{-2}$，
且 $j^5=O((1+\log\log(L+3))^5)$。
(1.4) 随之成立。

## 6. 尚不能据此排核的准确原因

(1.4) 只控制一个随 $L$ 收缩的全0柱投影。
它没有控制任意小测集，也没有控制所有物理柱的同一常数，
故不能直接调用 R165 的一致平方可积性障碍。

已知的全本质支撑只给
$\|\Pi_{0,L}|_{\mathcal M}\|>0$ 对每个有限 $L$ 成立。
这与随 $L$ 趋于0的定量上界相容。
没有使用“正数不能趋于0”一类错误推论，
也没有将 $A^r\mathcal M$ 稠密误当作存在统一有界的逆向柱转移。

因此本笔记完成的是：把全空间两孔向量替换为真实保 $\mathcal M$、幅度一致受控的多项式，
并给出核关系强制的实际柱投影衰减。
要排除一般慢共振，还需要额外建立柱投影下界、全测集一致性，或核方程提供的其他约束。
