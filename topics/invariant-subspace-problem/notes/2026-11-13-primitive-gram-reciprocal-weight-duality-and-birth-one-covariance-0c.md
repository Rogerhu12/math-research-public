# 任意出生层的 primitive Gram 倒数权反向对偶

- 日期：2026-11-13
- 作者：central_review、Astra-ISP-0c；AI 辅助：GPT-6 Astra Pro
- 状态：已证明；完整去权、容斥恒等、全逆后压缩及相邻反演次序均已逐式核验
- 范围：任意有限正权、全部合法出生层；只给精确对偶及其直接推论，不宣称一般相邻上界已经证明

## 1. 算子、整层逆与结论

在总位数为
$$
N
$$
的有限布尔 Hilbert 空间中，物理占据向量构成标准正交基。第 $s$ 孔层记为
$$
\mathcal H_s=\operatorname{span}\{e_I:|I|=s\}.
$$
正权删除算子为
$$
D_a=\sum_{i=1}^N a_iE_i,\qquad a_i>0.
$$
定义
$$
K_s(a)=\ker D_a\cap\mathcal H_s,\qquad
h=N-2s.
$$
下文只讨论
$$
0\le s\le \lfloor N/2\rfloor.
$$

对全部合法阶
$$
0\le n\le h,
$$
先在完整第出生层取逆，再压缩到 primitive 空间：
$$
F_n(a)=\frac{D_a^n(D_a^*)^n|_{\mathcal H_s}}{(n!)^2},
\qquad
\Gamma_n(a)=P_{K_s(a)}F_n(a)^{-1}|_{K_s(a)}.
\tag{1.1}
$$
这些整层逆全部存在，证明见第 2 节。

置
$$
b_i=a_i^{-1},\qquad
Z_{\mathrm{all}}=\prod_{i=1}^N a_i^2,
\qquad
a_I=\prod_{i\in I}a_i.
$$
定义真实子空间之间的线性同构
$$
B_s:K_s(a)\longrightarrow K_s(b),
\qquad
B_se_I=a_I^2 e_I
\quad\hbox{再限制于 }K_s(a).
\tag{1.2}
$$
这里的伴随按两个 primitive 子空间继承的原 Hilbert 内积计算。

**定理 1（全部出生层的精确反向对偶）。**
$$
\boxed{
\Gamma_n(a)=
Z_{\mathrm{all}}^{-1}
B_s^*\Gamma_{h-n}(b)B_s,
\qquad 0\le n\le h.
}
\tag{1.3}
$$

这不是原整层算子的直接对角相似恒等式。证明使用包含 incidence 与不交 incidence 之间的可逆自伴变换；该变换只有在取整层逆以后，对 primitive 输入才消为一个符号。

## 2. incidence、满射与有限去权

记不含权的包含 incidence 为
$$
C_{j,p}:\mathcal H_p\longrightarrow\mathcal H_j,
\qquad
(C_{j,p})_{J,P}=1_{\{J\subseteq P\}}.
$$
准确有
$$
C_{j,p}=\frac{D_1^{\,p-j}}{(p-j)!}.
\tag{2.1}
$$

当
$$
j\le p\le N-j,
$$
矩阵的转置单射，故 incidence 满射。这里可以直接用有限等权链分解：在第出生层，
$$
[D_1,D_1^*]=(N-2j)I.
$$
若单位 primitive 向量出生于第 $j$ 层，则其上升链的相邻系数是
$$
\sqrt{(\ell+1)(N-2j-\ell)}.
$$
在低半层，交换关系使 $D_1^*$ 单射，故其伴随删除满射，给出下面的 primitive 维数。各上升链由移伴随和 primitive 正交性相互正交，并且用
$$
\dim K_j(1)=\binom Nj-\binom N{j-1}
$$
逐层望远镜求和，穷尽全空间。处于第目标层的每条链，都可无零系数地继续上升到第源层，正是上述区间。因此完整 incidence 满射，包括两端。

在每个孔层定义有限可逆正对角算子
$$
T_p e_I=a_Ie_I.
$$
逐集合删除给
$$
D_a|_{\mathcal H_p}
=T_{p-1}^{-1}D_1T_p,
\qquad
K_s(a)=T_s^{-1}K_s(1).
\tag{2.2}
$$
令
$$
p=s+n.
$$
则
$$
\frac{D_a^n}{n!}
=T_s^{-1}C_{s,p}T_p.
$$
所以
$$
F_n(a)=T_s^{-1}M_aT_s^{-1},
\qquad
M_a=C_{s,p}T_p^2C_{s,p}^*.
\tag{2.3}
$$
由 incidence 满射与正权性，所有矩阵均严格正定可逆。对角去权只用来保持秩和写出准确矩阵，并未被当成酉相似。

对于倒数权，层对角算子是
$$
T_p(b)=T_p^{-1}.
$$
因而
$$
B_s=T_s^2|_{K_s(a)}
$$
准确把两个 primitive 空间互相映射。也可直接核验
$$
D_bB_s=B_{s-1}D_a.
\tag{2.4}
$$
它在这两个有限维空间之间可逆。

## 3. 包含与不交 incidence 的可逆变换

固定
$$
s\le p\le N-s.
$$
除包含 incidence 外，定义不交 incidence
$$
C'_{s,p}:\mathcal H_p\longrightarrow\mathcal H_s,
\qquad
(C'_{s,p})_{S,P}=1_{\{S\cap P=\varnothing\}}.
$$
补集酉映射记为
$$
J_p:\mathcal H_p\longrightarrow\mathcal H_{N-p},
\qquad
J_pe_P=e_{P^{\mathrm c}}.
$$
于是
$$
C'_{s,p}=C_{s,N-p}J_p.
\tag{3.1}
$$
两个 incidence 的转置都在本区间内单射。

定义完整第出生层上的算子
$$
\mathcal K_{s,p}
=
\sum_{j=0}^s
\frac{(-1)^j}{\binom{p-j}{s-j}}
C_{j,s}^*C_{j,s}.
\tag{3.2}
$$
全部二项式分母严格为正；该算子显然自伴。

**引理 2。**
$$
\boxed{
(C'_{s,p})^*=C_{s,p}^*\mathcal K_{s,p}.
}
\tag{3.3}
$$
并且
$$
\mathcal K_{s,p}\text{ 可逆},\qquad
\mathcal K_{s,p}|_{K_s(1)}=(-1)^sI.
\tag{3.4}
$$

给出逐集合证明。对任意第出生层向量，固定一个大小为第源层的集合。容斥恒等式
$$
1_{\{S\cap P=\varnothing\}}
=
\sum_{J\subseteq S\cap P}(-1)^{|J|}
$$
给出
$$
(C'_{s,p})^*
=
\sum_{j=0}^s(-1)^j C_{j,p}^*C_{j,s}.
\tag{3.5}
$$
另一方面，计算包含中间集合的数目得到
$$
C_{s,p}^*C_{j,s}^*
=
\binom{p-j}{s-j}C_{j,p}^*.
$$
代入即为 (3.3)。

如果变换有核，则由 (3.3) 得不交 incidence 的转置也有核，违反单射。因此变换可逆。若输入在不含权的 primitive 空间，则
$$
C_{j,s}x=0\quad(j<s),
$$
因为这些 incidence 是至少一次真实删除的幂。只剩最高项
$$
C_{s,s}=I,
$$
便得到符号公式 (3.4)。特别，
$$
\mathcal K_{s,p}^{-1}x=(-1)^s x
\qquad(x\in K_s(1)).
\tag{3.6}
$$

## 4. 补集、完整逆及 primitive 压缩

对倒数权取反向阶数
$$
n'=h-n,\qquad s+n'=N-p.
$$
其完整去权 Gram 为
$$
M_b=C_{s,N-p}T_{N-p}^{-2}C_{s,N-p}^*.
$$
对任意大小为第源层的集合，补集乘积恒等式给
$$
a_{P^{\mathrm c}}^{-2}
=Z_{\mathrm{all}}^{-1}a_P^2.
$$
因此由补集酉与 (3.1)，
$$
M_b
=Z_{\mathrm{all}}^{-1}
C'_{s,p}T_p^2(C'_{s,p})^*.
$$
由于变换自伴，(3.3) 也给
$$
C'_{s,p}=\mathcal K_{s,p}C_{s,p}.
$$
所以完整矩阵恒等式是
$$
M_b=
Z_{\mathrm{all}}^{-1}
\mathcal K_{s,p}M_a\mathcal K_{s,p}.
\tag{4.1}
$$
在完整空间取逆：
$$
M_b^{-1}
=
Z_{\mathrm{all}}
\mathcal K_{s,p}^{-1}
M_a^{-1}
\mathcal K_{s,p}^{-1}.
\tag{4.2}
$$

现在才读取 primitive 输入。若
$$
g,h_0\in K_s(a),\qquad
x=T_sg,\quad y=T_sh_0,
$$
则两个去权向量属于不含权的 primitive 空间。由 (2.3)，
$$
\langle\Gamma_n(a)g,h_0\rangle
=
\langle M_a^{-1}x,y\rangle.
\tag{4.3}
$$
倒数权的去权向量也恰好相同：
$$
T_s(b)B_sg=T_sg=x.
$$
利用 (4.2) 和 (3.6)，两个符号相消，得到
$$
\begin{aligned}
\langle\Gamma_{n'}(b)B_sg,B_sh_0\rangle
&=\langle M_b^{-1}x,y\rangle\\
&=Z_{\mathrm{all}}\langle M_a^{-1}x,y\rangle.
\end{aligned}
$$
这就是 (1.3)。全证明始终先使用完整逆；没有把 primitive 压缩与逆交换。

## 5. 端点和相邻算子序的准确次序

零阶是 primitive 空间的恒等。令反向阶为零，定理给出显式最高阶：
$$
\boxed{
\Gamma_h(a)=
Z_{\mathrm{all}}^{-1}B_s^*B_s
=
Z_{\mathrm{all}}^{-1}
P_{K_s(a)}
\operatorname{diag}(a_I^4)|_{K_s(a)}.
}
\tag{5.1}
$$
这包括真空出生和最高合法出生，不需要额外极限。

对
$$
1\le n<h,\qquad m=h-n,\qquad c>0,
$$
对偶把相邻比较
$$
\Gamma_n(a)\Gamma_{n+1}(a)^{-1}\Gamma_n(a)
\le c\,\Gamma_{n-1}(a)
\tag{5.2}
$$
准确化为
$$
\Gamma_m(b)\Gamma_{m-1}(b)^{-1}\Gamma_m(b)
\le c\,\Gamma_{m+1}(b).
\tag{5.3}
$$
这里的邻居顺序确实已经反向，不能直接略去。

对任意三个严格正算子，有准确等价
$$
A B^{-1}A\le cC
\quad\Longleftrightarrow\quad
A C^{-1}A\le cB.
\tag{5.4}
$$
证明只需对正算子不等式取逆，再作同余；严格不等式也同样等价。
因此 (5.3) 又等价于通常次序的
$$
\Gamma_m(b)\Gamma_{m+1}(b)^{-1}\Gamma_m(b)
\le c\,\Gamma_{m-1}(b).
\tag{5.5}
$$
常数保持不变。

## 6. 已证两异权全出生族的进一步上界

[两异权全出生定理](../results/R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)的两个任意正头权加同一等权池，在倒数权下仍在同一家族中。
已证全部出生层的相邻系数为
$$
c_{s,n}=\frac{s+n}{s+n+1}.
$$
分别在原权和倒数权的反向阶应用该定理，再用第 5 节，得到
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
<
\min\!\left\{
\frac{s+n}{s+n+1},
\frac{N-s-n}{N-s-n+1}
\right\}\Gamma_{n-1}.
}
\tag{6.1}
$$
这是两个已证系数的较小值，不是此前已经被反例否定的有限总位数乘积因子。

对任意正异权，一般相邻上界的真假仍未由精确对偶解决。
本结果只使反向阶的比较完全等价，并给出准确最高阶公式；它不把非交换的中间 Gram 当成标量比，也没有对原无限尾的 Schur 返回费用作未经证明的运输。


## 7. 出生一层的条件子集协方差与准确正网络

本节给出第 $s=1$ 层的另一套具体坐标；它独立核对前面的对偶，也保留研究一般相邻不等式所需的完整 Schur 项。

设 $N\ge2$，记
$$
A=\operatorname{diag}(a_1,\ldots,a_N),\quad
z_i=a_i^2,\quad
a=(a_1,\ldots,a_N)^{\mathsf T},\quad
K=a^\perp.
$$
取 $k=n+1$，所以 $1\le k\le N-1$。
在全部 $k$ 元子集上定义一个准确的概率分布
$$
\mathbb P_k(S)=\frac{z_S}{e_k(z)},\qquad
z_S=\prod_{i\in S}z_i.
\tag{7.1}
$$
令 $I_S\in\{0,1\}^N$ 是占据列向量，
$$
\pi_k=\mathbb E_k I_S,\qquad
\mathsf C_k=\mathbb E_k(I_SI_S^*)-\pi_k\pi_k^*.
$$
因为 $|S|=k$ 固定，$\mathsf C_k\mathbf1=0$。

对任意 $x\in\mathcal H_1$，真实上升公式为
$$
\frac{(D_a^*)^n}{n!}x
=
\sum_{|S|=k}a_S
\left(\sum_{i\in S}\frac{x_i}{a_i}\right)e_S.
$$
因此完整整层 Gram 是
$$
F_n=e_k(z)A^{-1}\mathbb E_k(I_SI_S^*)A^{-1}.
\tag{7.2}
$$
特别，
$$
F_na=k\,e_k(z)A^{-1}\pi_k,\qquad
a^*F_na=k^2e_k(z).
$$

定义在整层上以零延拓的 Schur 算子
$$
\widetilde Q_n
=
F_n-\frac{F_na\,a^*F_n}{a^*F_na}.
\tag{7.3}
$$
它的核为 $\mathbb Ca$，其在 $K$ 上的限制正是
$\Gamma_n^{-1}$：按 $K\oplus\mathbb Ca$ 作普通块逆，
$(P_KF_n^{-1}|_K)^{-1}$ 是上述 Schur 补。由 (7.2) 得
$$
\boxed{
\widetilde Q_n
=e_k(z)A^{-1}\mathsf C_kA^{-1},
\qquad
\Gamma_n^{-1}=\widetilde Q_n|_K.
}
\tag{7.4}
$$
因此协方差形式来自完整逆后压缩，不能将 $\Gamma_n^{-1}$ 直接写成 $P_KF_n|_K$。

### 7.1 完整图上的正边权

记 $e_j^{(ij)}$ 为删去 $z_i,z_j$ 后的初等对称和，约定 $e_0^{(ij)}=1$、越界下标为零。对 $i\ne j$，
$$
\pi_{k,i}=\frac{z_i e_{k-1}^{(i)}}{e_k},\qquad
\mathbb P_k(i,j\in S)=\frac{z_iz_j e_{k-2}^{(ij)}}{e_k}.
$$
故 $e_k\mathsf C_k$ 是完整图的 Laplacian，边权准确为
$$
\boxed{
\omega_{ij}^{(k)}
=
\frac{z_i z_j}{e_k(z)}
\left[
\bigl(e_{k-1}^{(ij)}\bigr)^2
-e_k^{(ij)}e_{k-2}^{(ij)}
\right]>0.
}
\tag{7.5}
$$
展开
$$
e_k=e_k^{(ij)}+(z_i+z_j)e_{k-1}^{(ij)}
+z_iz_j e_{k-2}^{(ij)}
$$
及
$e_{k-1}^{(i)}=e_{k-1}^{(ij)}+z_j e_{k-2}^{(ij)}$
即可逐项核对 (7.5)，所有含 $z_i,z_j$ 的额外交叉项相消。

严格正性也可直接核验。中间下标用实根多项式
$\prod_{\ell\ne i,j}(1+z_\ell t)$ 的 Newton 不等式；
该不等式由其逐次导数仍有负实根、以及
$Q'(0)^2-Q(0)Q''(0)>0$ 得到。端点 $k=1$ 时括号为 $1$，
$k=N-1$ 时括号为 $(e_{N-2}^{(ij)})^2$，同样严格正。
所以对 $x\in K$，
$$
\boxed{
\langle\Gamma_n^{-1}x,x\rangle
=
\sum_{i<j}\omega_{ij}^{(k)}
\left|\frac{x_i}{a_i}-\frac{x_j}{a_j}\right|^2.
}
\tag{7.6}
$$

补集把 (7.1) 的 $z$ 权、$k$ 元子集分布准确变成
$z^{-1}$ 权、$N-k$ 元子集分布；其协方差相同，且
$e_k(z)=Z_{\mathrm{all}}e_{N-k}(z^{-1})$。
这与第 4 节的全部出生层对偶一致。

(7.4)—(7.6) 是确定的正形式与网络表达。逐条边权的标量正性不自动给出不同 $n$ 之间的非交换算子序；一般相邻界仍需要额外证明。
