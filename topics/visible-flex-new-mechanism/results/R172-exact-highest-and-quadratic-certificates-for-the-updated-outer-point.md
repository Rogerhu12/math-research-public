# R172：新外点的最高层与二次层精确证书，以及剩余真实性问题

日期：2026-11-15。**已证明。** 本稿只读取已发有理外点并作纸面平方展开，不运行 Gram 优化、profile 评价、路径积分或重复人工检查。

依据 [R164](R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)、[R167](R167-four-monomial-Gram-certificate-for-complete-highest-action.md)、[R168](R168-reflection-of-corrected-low-action-and-four-head-relations.md) 及 [联合 static/parity actual](../notes/character-minus2-static-parity-actual-20261115.md)。

本次外点仍未被证明是 U 上的真实泛函。本稿证明的是它所给出的**完整修正 action 系数**的准确解析性质：最高层在全部真实平端路径上的积分非负，二次层逐点正定。它当前仍因静态函数取负而不能是正字符。若后继点保持这两个修正层、并把静态层准确变为全局非负，则任何路径非负性条件都不能再排除那个点；是否存在对应真实泛函，必须由原函数关系判断。

## 1. 实际来源与准确系数

新点来自公开 run [43668125602](https://github.com/Rogerhu12/math-research-public/actions/runs/43668125602)，源提交 c8a89721ee361074096b202af6aa0841ac1bc445，lane character_minus2_static_parity。

目录为

    notes/actions-43668125602-1-character_minus2_static_parity/

主报告 character-minus2-static-parity.json 为 6971 字节，SHA256
bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968。
完整有理证书 character-minus2-static-parity-certificate.json.gz 为 9222 字节，SHA256
2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af；
原始 34807 字节，SHA256
f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23。

该证书的 decision.outer_candidate 保存 23 个旧自由坐标中的准确有理点，须结合其绑定的旧 RREF 解释为 107 个 normal 坐标。此前联合续算已验证它满足新增静态行和完整二次奇偶，且没有重建旧根或旧积分。本稿不把这一外部可行性提升为真实字符存在。

在 R164 的完整修正坐标中，静态函数是

$$
C(k)=\frac{11}{48}-\frac{59}{48}k^2+k^4+k^6.
\tag{1}
$$

三个二次系数是

$$
b_0(k)=1+k^2,\qquad
b_1(k)=-k-k^3,\qquad
b_2(k)=1+k^2+k^4.
\tag{2}
$$

按 R165/R167 的最高层十数顺序，

$$
\boxed{(a,b,c,d,e,f,g,j,\ell,m)
=(1,1,-1,1,-1,-1,1,-1,1,1).}
\tag{3}
$$

此处最高加速度系数 a=1，与静态函数在 k=0 的值 $C(0)=11/48$ 不同。R164 的同一规范化乘子是

$$
\mu=(0,11/24,2,0,0,0,0,11/6).
\tag{4}
$$

以下始终使用已经扣掉 (4) 的完整修正二次层，不给各项另选乘子。

## 2. 全部最高 action 的精确平方证书

令

$$
r=\log h,\quad v=r',\quad z=v'+v^2,\quad \rho=e^{-2r},
\quad y=e^{-r}k,
$$

$$
Z=(Z_1,Z_2,Z_3,Z_4)^T=(y'',v y',v'y,v^2y)^T.
\tag{5}
$$

将 (3) 代入 R167 的矩阵，并选择准确常参数

$$
\theta=\eta=-1,
$$

得到

$$
G_{-1,-1}=
\begin{pmatrix}
1&1/2&1/2&-1\\
1/2&3&1&-1/2\\
1/2&1&1&-1/2\\
-1&-1/2&-1/2&2
\end{pmatrix}.
\tag{6}
$$

它有以下完整有理平方分解：

$$
\boxed{\begin{aligned}
Z^TG_{-1,-1}Z={}&
\left(Z_1+\frac12Z_2+\frac12Z_3-Z_4\right)^2\\
&+\frac{11}{4}\left(Z_2+\frac3{11}Z_3\right)^2
+\frac6{11}Z_3^2+Z_4^2.
\end{aligned}}
\tag{7}
$$

因此该矩阵实际上正定，不是未经核对的近似半正定输出。式 (7) 只是十个有理系数的直接纸面展开。

R167 的完整点态身份在这里是

$$
L_4=\rho(z^2+v^4)+Z^TG_{-1,-1}Z
+\frac{d}{ds}\left[v(y')^2+v^2yy'+v^3y^2\right].
\tag{8}
$$

全部 H1、H2 项仍在式 (6)–(8) 内。真实平端 h 给两端 $v=0$，故方括号在两个端部各自为零；不用两端状态相同。于是对任意真实有限平端路径，

$$
\boxed{\int L_4\,ds
=\int\rho(z^2+v^4)\,ds+\int Z^TG_{-1,-1}Z\,ds\ge0.}
\tag{9}
$$

这里证明的是完整最高层的积分非负；原点态 $L_4$ 含有已支付的导数项，不能由 (9) 宣称其每个点都非负。

## 3. 完整修正二次层逐点正定

在 R164 的 r、k 变量下，二次密度为

$$
A_2=\rho\left[
b_2(k)(r')^2+b_1(k)r'k'+b_0(k)(k')^2
\right].
\tag{10}
$$

代入 (2)，直接配方：

$$
\boxed{
A_2=\rho\left[
(1+k^2)\left(k'-\frac{k}{2}r'\right)^2
+\left(1+\frac34k^2+\frac34k^4\right)(r')^2
\right].
}
\tag{11}
$$

两个系数对所有实 k 都严格正。因此 $A_2>0$ 当且仅当速度 $(r',k')\ne(0,0)$；零速度时它为零。

等价地，令 $x=k^2\ge0$，对应矩阵的行列式为

$$
\det
\begin{pmatrix}
1+x+x^2&-k(1+x)/2\\
-k(1+x)/2&1+x
\end{pmatrix}
=(1+x)\left(1+\frac34x+\frac34x^2\right)>0.
\tag{12}
$$

这是完整修正二次层的结论，不是把任意真实正字符都预先要求为逐点二次 PSD。其他候选仍可能依靠静态和最高层的耦合允许负的二次密度。

## 4. 当前点仍因静态负值被排除

当前静态函数准确分解为

$$
C(k)=\left(k^2-\frac14\right)
\left(k^4+\frac54k^2-\frac{11}{12}\right).
\tag{13}
$$

它在先前加入的 k=1/2 测试处为零，但在

$$
\boxed{k=\frac23,\qquad C(2/3)=-\frac{371}{11664}<0.}
\tag{14}
$$

取任意常 h>0、常 k=2/3 的有限正时长路径，真实 $\omega$ 也是常值。所有导数项消失，完整修正 action 恰为时长乘 $h^{-2}C(2/3)$，严格为负。末 frame 无须预设为 I，因为 R140 的同一乘子条件已经覆盖所有真实开平端路径。

所以 (9)、(11) 并不挽救当前外点；它仍不能代表真实正字符。它们说明对这个点再搜索最高层或二次层的负路径没有必要，当前未付路径条件明确位于静态层。静态候选解析分离由后继独立 consumer 处理，本稿不重复其求解。

## 5. 何时必须转向真实原函数关系

考虑以后某个准确外坐标点：在同一 R164 定义下，它保持 (2) 的**修正二次层**和 (3) 的最高层，并有一个对所有实 k 非负的修正静态函数 $\widetilde C(k)$。它的同一矩阵乘子也须按其静态值与原规范化一致确定；这里不是建议独立改写原算子的不同系数。

由 (9)、(11)，对每条真实有限平端路径都有

$$
\begin{aligned}
\mathcal A
={}&\int \rho\,\widetilde C(k)\,ds+\int A_2\,ds+\int L_4\,ds\\
&\ge0.
\end{aligned}
\tag{15}
$$

这覆盖所有路径、所有转向和所有时长，而不只覆盖已采样的固定轴或六条多项式路径。所有额外端势仍由 (8) 支付。

因此，在 (15) 的条件下，继续增加任何**合法的路径非负性必要条件**都无法切掉该点。若它不是真实字符，缺口只能在尚未表达的真实算子关系、头部商关系或其对应泛函的良定义性上；不能靠另换一个路径网把一个实际非负的标量 action 变负。

反过来，若后继能证明该点确实给出 U 上的非零真实仿射字符，R140/R164 才把 (15) 提升为实际成本闭锥的正泛函。当前没有这样的真实性证明。本稿既不授真实正字符存在，也不授完整 period/ruling 的阻碍或消除结论。

新结果使后继任务有明确分界：静态函数仍负时使用其准确负点；完整标量 action 已由精确证书非负时，转向已发原根的真实线性关系，不能把外坐标可行误当真实泛函可行。
