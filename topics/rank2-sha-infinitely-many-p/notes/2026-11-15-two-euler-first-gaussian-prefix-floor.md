# 两个完整 Euler 输出的第一 Gaussian 前缀下界

日期：2026-11-15。**状态：以下针对指定分歧首层方案的下界已证明。** 在原来源和原逐列分歧缩放下，即使两个输出的联合合流矩阵具有可能的最大秩，用第一 Gaussian 的模 $\pi$ 矩阵证明一个共同连续前缀单射，仍至少需要
$$
k\ge\left(\frac{441}{400}-o(1)\right)D^2.
$$
这个常数严格大于旧低 $\ell$ 维数临界的 $47/48$。本条因此排除一个具体的辅助素数证明方案；不排除真正 regular 高尾、改变带权饱和步骤或直接分析目标素数的原短矩阵。

## 1. 一个完全由原列组成的余类

保持 [R657](../results/R657-original-long-ordered-prefix-and-quadratic-contact-bound.md) 的全部来源和规范：
$$
p_{\rm aux}=6s-1>101,\qquad
f_D=\lfloor9D/2\rfloor+4<p_{\rm aux},
$$
$$
\mathcal W_D=\bigoplus_{n=0}^{D}Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
A_n=\lfloor(n+1)/4\rfloor,\quad b_n=A_n+e_{n+1},
$$
其中 $q_n$ 是原十九角分式，所有自由幂仍受原 $e_{n+1}$ 限制。
原列 $Y^nq_nt^a$ 的物理首阶为
$$
r_{n,a}=13+A_n+a.
$$
观察同一向量的两个完整输出
$$
\Phi(P),\qquad\Phi(\mathcal EP),\quad\mathcal E=Y\partial_Y,
$$
其中 $\Phi$ 完整保 $w^{13}$、$P_{134}/U_0$ 和公共 charge 四十。

设
$$
u_*=13+A_D<s.
\tag{1}
$$
这个条件在下文的渐近范围自动成立；有限参数使用时明确保留。
在余类 $u_*\bmod s$，第 $n$ 个节点的**实际原列**准确为
$$
a=A_D-A_n+js,\qquad
0\le j\le J_n^*:=
\left\lfloor\frac{b_n-A_D}{s}\right\rfloor.
\tag{2}
$$
当 $J_n^*<0$ 时该节点没有列。确实，$A_n\le A_D$ 使 (2) 的下帽非负，
而 $a\le e_{n+1}$ 恰等价于 $A_D+js\le b_n$。
因 $u_*<s$，不存在遗漏的负 $j$。因此这里不曾补齐环境列。

置
$$
\boxed{C_*=\sum_{n=0}^{D}(J_n^*+1)_+.}
\tag{3}
$$
这是同一个原余类中真实存在的列数。

## 2. 同一分歧首层的必要行数

取 $\pi^s=p_{\rm aux}$、$w=\pi z$。
R646/R657 已证明：保留全部 regular 高尾后，每条原列按
$\pi^{-r_{n,a}}$ 缩放是整的，其模 $\pi$ 准确为
$$
\lambda_{n,a}z^{u_*+js}
e^{\bar a_p(n+40)z^s},\qquad \lambda_{n,a}\in k^\times.
$$
第二输出多乘原整数 $n$。因此 (2) 的两个联合输出在首层都只占据
普通行号 $u_*+hs$。

若每个输出只读连续前缀 $0\le m<k$，该余类在每个输出中的行数为
$$
H(k,u_*)=\max\left\{0,\,
1+\left\lfloor\frac{k-1-u_*}{s}\right\rfloor\right\}.
$$
这 $C_*$ 条原列在两个首层输出中的秩至多 $2H(k,u_*)$。
所以任何声称该归一矩阵模 $\pi$ 全列单射的证明，都必须满足
$$
2H(k,u_*)\ge C_*.
$$
当 $C_*>0$ 时，准确的整数必要条件为
$$
\boxed{
k\ge u_*+s\left(\left\lceil\frac{C_*}{2}\right\rceil-1\right)+1.
}
\tag{4}
$$
其它余类的行不能提高这组首层列的秩。任意可逆的模 $\pi$ 行列变换也不能绕过 (4)。

这里只使用必要的行数。没有假定联合合流矩阵真的达到最大秩；
若它有额外关系，所需前缀只会更长。

## 3. 所有允许辅助比例的准确最小主常数

令 $D\to\infty$，先取一个满足
$$
p_{\rm aux}/D\longrightarrow\alpha,\qquad \alpha\ge9/2
\tag{5}
$$
的子列。后一个限制正来自原 $f_D<p_{\rm aux}$，不能为优化常数而删除。

原十二余类帽给
$$
A_D=D/4+O(1),\qquad b_n=25n/6+O(1)
$$
且后一误差对 $0\le n\le D$ 一致。
将 (3) 改写为逐 $j$ 计数：
$$
C_*=\sum_{j\ge0}\#\{0\le n\le D:b_n\ge A_D+js\}.
$$
由 (5)，仅有限个 $j$ 有贡献，并且
$$
\boxed{
\frac{C_*}{D}\longrightarrow
\sum_{j\ge0}\left(\frac{47}{50}-\frac{\alpha j}{25}\right)_+.
}
\tag{6}
$$
这里的 $47/50$ 来自真实下帽 $A_D$；
不能把它换成补齐族的常数一。

(4) 因而给
$$
\liminf\frac{k}{D^2}\ge
F(\alpha):=\frac{\alpha}{12}
\sum_{j\ge0}\left(\frac{47}{50}-\frac{\alpha j}{25}\right)_+.
\tag{7}
$$

**引理。**
$$
\boxed{\min_{\alpha\ge9/2}F(\alpha)=\frac{441}{400}.}
\tag{8}
$$

**证明。** 置 $B=47/50$。
在贡献的最大正整数 $j$ 不变的每个区间，
$$
F(\alpha)=\frac{\alpha}{12}
\left((j+1)B-\frac{\alpha j(j+1)}{50}\right)
$$
是凹二次式。因此区间上的最小值在端点。
除左端 $\alpha=9/2$ 外，全部有限分段端点为
$$
\alpha=\frac{47}{2j},\qquad j=1,\ldots,5.
$$
在这些点，
$$
F\!\left(\frac{47}{2j}\right)
=\frac{2209}{2400}\left(1+\frac1j\right)
\ge\frac{2209}{2000}.
$$
在最后的线性区间 $j=0$，函数随 $\alpha$ 增加。
而在左端，
$$
\sum_{j=0}^{5}\left(\frac{47}{50}-\frac{9j}{50}\right)
=\frac{147}{50},
$$
所以
$$
F(9/2)=\frac{3}{8}\cdot\frac{147}{50}
=\frac{441}{400}
<\frac{2209}{2000}.
$$
这覆盖全部端点和区间，证明 (8)。证毕。

若允许的辅助比例 $p_{\rm aux}/D$ 无界，则 (3) 至少含
$(47/50+o(1))D$ 个真实 $j=0$ 列。
(4) 直接给 $k/D^2\to\infty$ 沿该子列。
所以取子列后的论证也支付了不收敛、甚至无界的任意辅助素数选择。

结合 (7)–(8)，得到对所有允许辅助选择统一的必要下界
$$
\boxed{
k\ge\left(\frac{441}{400}-o(1)\right)D^2.
}
\tag{9}
$$
这是一个必要下界，不声称 $\alpha=9/2$ 时实际存在达到它的单位子式，
也不为该结论使用目标素数扫描。

## 4. 对原临界问题的精确含义

低 $\ell$ 下原来源维数为
$$
\dim\mathcal W_D=\frac{47}{24}D^2+O(D).
$$
旧两长块的维数平衡为
$$
s=\left(\frac{47}{48}+o(1)\right)D^2.
$$
而
$$
\boxed{
\frac{441}{400}-\frac{47}{48}=\frac{37}{300}>0.
}
\tag{10}
$$
因此，即使把 R657 两输出增补中的逐层剥离改进到每个联合合流块的最大可能秩，
仅靠同一个第一 Gaussian 分歧首层，仍不能把共同前缀压到旧临界长度。

(9) 排除的只有这一具体首层方案：

- 仍用 R646/R657 的原逐列权和两个完整输出；
- 通过其模 $\pi$ 第一 Gaussian 矩阵中的单位列满秩子式证明前缀单射；
- 不再利用首层关系经除 $\pi$ 后产生的真实 regular 高尾。

如果改变带权饱和步骤、对首层关系继续读取下一位，或者直接使用原目标素数下
$g/t/q_n$ 的真实高尾，(4) 不给这些新方法的限制。
同样，本条不是原短矩阵在目标素数处确有核或确有非零 $d_2$ 的证明。

原完整 $M$ 的两条十三行、同一个修正 $R$、完整第二 forcing，
以及三条原算术中央条件均保持原样。
R637 的平方根整满射范围之外，仍须处理这些实际来源的原短像。
