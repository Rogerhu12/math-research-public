# R380：十六个真实目标的同一有限根支付完整 Y 平方

日期：2026-11-15。完整有限纸面证明；未执行求积、符号程序、人工研究检查或参数搜索。

本稿把 R377 已准确消去的 $YY_0$ 角商与 R376 的十五目标真实控制器接合。新增的是同一圆上的一个完整 $\pi/2$ 值；不添加假 $C^2$ 费用，不把主行的独立性单独当成完整角函数已付。十六个真实形状组、192个实际正幅列及一个有限频率的共同根，支付整个 $Y^2$，同时保持先前八个完整对称乘积、18个面积、原 $\mathcal T,\Psi$ 与三条 $F$ 行。

唯一尚未完整支付的对称乘积为 $Z^2$ 的第2外矩。该项的额外角商必须另核、另付；本稿不授完整第四 period 或同一固定几何。

来源：
[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、
[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R364](R364-local-angular-quotient-and-five-target-control-pay-the-negative-three-minus-one-product.md)、
[R375](R375-exact-Y-second-cubic-and-thirteen-target-control-pay-ZY2-and-YY2.md)、
[R376](R376-cubic-cross-identities-and-fifteen-target-cone-pay-ZY0-and-WY1.md)、
[R377](R377-complete-YY-zero-angular-quotient-and-local-C2-quartic.md)。

## 1. 完整额外角商已经由原18面积为零

保持原全偶真实弱圆
$$
\phi=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-\phi\odot\phi,\qquad q=f+ig.
$$
整个 $q$ 的三个双线性矩 $I_j(q,q)$ 均为零，所以原 $Y(q,q)$ 真紧。单个 nonlegal 强微包没有这个性质；以下角商恒等只用于整个合法 $q$。

按 R376 的同一 $I$ 规范，原完整角商为
$$
K_{YY,0}=DF_{Y,0}[Yq^2].
$$
R377 的无除 $x$ 完整变分及 R349 的原 primitive/Green 恒等给
$$
3F_{Y,0}=F_{U,2}-F_{L,2},\qquad
K_{YY,0}=\frac{S_{UY,2}-S_{LY,2}}3,
$$
$$
S_{UY,2}=-5S_{LY,2}.
$$
因为 $Z=dL+eU$，有
$$
\boxed{K_{YY,0}=-\frac{2S_{ZY,2}}{d-5e}=0.}
\tag{1}
$$
分母
$$
d-5e=\frac{\kappa(99\kappa^2+5)}{4h_e}>0
$$
且原18个完整面积已经给 $S_{ZY,2}(q)=0$。此处消费的是完整已付身份，不只比较最高导数项。

原真实十二副本已清除不匹配的交叉谐波，故 R294/R377 的完整角分解准确化为
$$
\boxed{\mathcal Q_{YY,0}(\theta)
=\sin^2\theta\,\mathcal Q_{YY,0}(\pi/2).}
\tag{2}
$$
全偶反射给 $YY_1=0$，R375 的同点根已经给整个 $YY_2=0$。只需将(2)右侧的一个真实值加入末控制器。不能把仅在实 profile 上的局部四次式正性搬成合法复圆的障碍，也无需为(1)添加新的纤维观察。

## 2. 新增主行与十六行严格独立

记号采用下列准确约定：
$$
v=u',\qquad r=u'',\qquad t=u'''.
$$
原固定系数与主行仍为
$$
\alpha_P=-2r,\qquad
\alpha_W=2av-2(a+b)xr,
$$
$$
\alpha_Z=du+(2e-d)xv-3ex^2r,\qquad
\alpha_Y=x^2u-x^3v+\frac12x^4r.
\tag{3}
$$
$a,d,e,d+6e$ 均非零。R285 的完整分裂对新增行给
$$
\mathcal Q_{YY,0}(\pi/2)
\equiv_2\sum_i\lambda_i\int\alpha_Y^2t^2,
\qquad
\lambda_i=-a_i^2(a_i^2-b_i^2).
\tag{4}
$$
$\equiv_2$ 保留原完整 Green、primitive、有序尾及实际基线的连续 $C^2$ 余项；这些余项在最后真实根中共同处理，不在(4)里设为零。

原十五个多项式逐字保为
$$
\begin{gathered}
r^2,\ x^2r^2,\ xvr,\ ur,\\
x^2\alpha_P\alpha_Z,\ \alpha_P\alpha_Y,\
x^2\alpha_P\alpha_Y,\ x\alpha_Z\alpha_W,\
\alpha_Z^2,\ \alpha_W^2,\ x^2\alpha_W^2,\\
x^2\alpha_Z\alpha_Y,\ x^2\alpha_Y^2,\
\alpha_Z\alpha_Y,\ x\alpha_W\alpha_Y.
\end{gathered}
\tag{5}
$$
本稿只添
$$
p_{16}=\alpha_Y^2.
\tag{6}
$$
赋权 $(x,u,v,r)=(1,2,1,0)$ 后，旧表在权
$0,2,4,6,8,10$ 的行数为 $1,4,5,3,1,1$。
(6)只有权8；与它同权的旧行是 $x^2\alpha_Z\alpha_Y$。

若这两行线性相关，实多项式环无零因子且 $\alpha_Y\ne0$，便有
$$
A\alpha_Y+B x^2\alpha_Z=0.
$$
比较 $x^2u,x^4r$ 的两列，
$$
\det\begin{pmatrix}1&1/2\\d&-3e\end{pmatrix}
=-\frac{d+6e}{2}\ne0.
\tag{7}
$$
故 $A=B=0$。结合 R376 已逐组证明的其余各权独立，得到十六行独立，分组数为
$$
\boxed{1,\ 4,\ 5,\ 3,\ 2,\ 1.}
\tag{8}
$$
最高位置次数仍为10；新增行自身的位置次数为8。这里没有增加十二点差分的次数范围。

## 3. 同一个真实正偶母与16个有限形状

必须把(8)转换为同一个母函数的数据，不能将形式变量 $u,v,r$ 当成一条函数上的自由参数。直接复用 R376 §§7–8 已证明的完整真实 copy 与有限 jet 引理，维数由15改为16；其假设在本稿逐项满足如下。

先固定原有限编码、所有实际副本相对位移 $d_\nu$、正四次权 $\omega_\nu$ 和面积平衡 blocks。它们的相对数据在选母以前即可固定；不将它们换成同心模型。十六行均满足
$$
p(-x,u,-v,r)=p(x,u,v,r).
$$
因此实际偶配对作用是
$$
\mathscr A p(y,u,v,r)=
\frac12\sum_\nu\omega_\nu
\{p(y+d_\nu,u,v,r)+p(y-d_\nu,u,v,r)\}.
\tag{9}
$$
在位置次数至多10的整个多项式空间上，(9)逐阶三角，主对角都是
$W_c=\sum_\nu\omega_\nu>0$，所以可逆。它保十六行独立，而不要求实际偏移的奇矩为零。

在开放集合
$$
0<y<1/2,\quad U>0,\quad R>0,\quad V\in\mathbb R
$$
上，十六维点值向量
$\mathscr A\mathbf p(y,U,V,R)$ 张成全 $\mathbb R^{16}$：否则某个非零线性组合多项式在实开集恒零，违反(8)及(9)。有限评价引理因而给十六组互异的实际 $y_i$ 及正 $U_i,R_i$，使点值矩阵可逆；排除有限个重复 $y_i$ 不改变开放集论证。

取原
$$
\psi(y)=\exp[-1/(1-y^2)]\quad(|y|<1)
$$
及外部零延拓。在 $\pm y_i$ 为偶多项式 $H$ 指定
$$
H=\log(U_i/\psi),\quad
H'=V_i/U_i-(\log\psi)',\quad
H''=R_i/U_i-(V_i/U_i)^2-(\log\psi)''.
\tag{10}
$$
有限 Hermite 插值实现这些二阶 jets，$\psi e^H$ 为同一个正偶母。用足够高但有限次数的偶多项式逼近正 prefactor，保严格 determinant 与正性。

从起点仍保原有限观察
$$
\mathcal F_{\rm new}=
(\mathcal F_\star,\text{全部 }\mathfrak j,\mathfrak k
\text{ 的真实平移系数}).
\tag{11}
$$
原类的最大微分 minor 与固定纠正方向先选好；沿它与上面正见证之间的有限多项式直线，该 minor 是非恒零多项式。在正见证任意小邻域避开有限个零点，便可同时保(10)的严格点值 determinant、正 prefactor、$u_0''(0)\ne0$ 与原最大 minor。

最后在16对点附近选足够窄但有限的偶 cutoff，再按 R376 用 $\psi$ 乘偶多项式逼近，得到16个实际固定 $\chi_\alpha$，使
$$
\left[
\sum_\nu\omega_\nu\int
\mathbf p(d_\nu+y,u_0,u_0',u_0'')
\chi_\alpha(y)^2\,dy
\right]_{\alpha=1}^{16}
\tag{12}
$$
可逆。所有列来自同一个 $u_0$，没有拼接不同母的观察值，也没有把点质量作为最终形状。

## 4. 192个实际列及严格正核

每个形状组使用原编码一个不同层的12个实际交替索引
$$
0,1,33,34,49,50,65,66,81,82,97,98.
\tag{13}
$$
原至少2048层足够提供16个不同组。真实副本和镜像共享同一个扰动参数。

每组的实际递增坐标 $X_i$ 对应
$$
\beta_i=\frac1{\prod_{k\ne i}(X_i-X_k)},\qquad
\beta_i/\lambda_i>0.
\tag{14}
$$
完整主列为
$$
v_{\alpha i}=\frac{\lambda_i}{2}
\sum_\nu\omega_\nu\int
\mathbf p(X_i+d_\nu+y,u_0,u_0',u_0'')
\chi_\alpha^2\,dy.
\tag{15}
$$
除 $\lambda_i/2$ 后，每个分量是 $X_i$ 的至多10次多项式。十二点 barycentric 身份与(14)故给每组一个全分量严格正的核；合起来是192维严格正核。它只消次数不超过10的实际多项式，不是十六阶差分。

若某行 covector 消灭全部192列，它在每个形状组上的位置多项式有12个不同零点，故恒零。取其形式值 $X=0$，由(12)迫该 covector 为零。因此
$$
\boxed{\operatorname{rank}(v_{\alpha i})=16,\qquad
\ker(v_{\alpha i})\cap\mathbb R_{>0}^{192}\ne\varnothing.}
\tag{16}
$$
由满行秩和严格正核，实际非负锥为整个 $\mathbb R^{16}$。这一步给了正幅可达性，不能用 signed span 取代。

## 5. 一个有限 N 同时支付全部旧目标和 YY0

仍回到末端控制器以前的同一个实际入口：弱 rank-two 核、宽 cutoff、补矩、所有旧宏块、全部18面积及 $\mathcal T=0$ 已固定，保留负 $\Psi$ 储备。按上述顺序选母、真实 copy、最终中心和固定纠正方向，再以原强块静态正幅准确支付 $\Psi$。

每个选中微包只作原合法扰动
$$
u_{N,z}=u_0+N^{-3}z\chi_\alpha\cos Ny
+\sum_\ell a_\ell(N,z)e_\ell,\qquad
\mathcal F_{\rm new}(u_{N,z})=\mathcal F_{\rm new}(u_0).
\tag{17}
$$
固定正幅盒上，原常秩纠正及参数一导在 $C^2$ 是 $O(N^{-1})$。固定光滑纠正方向的三导贡献同阶；平方振荡及参数一导给(15)，交叉振荡趋零。原连续 $C^2$ 余项及其参数一导趋向完整真实基线。

取 R376(38)的十五个真实目标 $\mathbf G^{15}$，逐字保它们的顺序和规范，定义
$$
\mathbf G^{16}=(\mathbf G^{15},\mathcal Q_{YY,0}(\pi/2)).
$$
前四行仍只作原固定可逆变换。R285 的完整保尾分裂及原有序加法给
$$
\mathbf G^{16}_N(\mathbf z)
=\mathbf G^{16}_{\rm base}
+\sum_{\alpha,i}z_{\alpha i}^2v_{\alpha i}
+o_{C^1}(1).
\tag{18}
$$
基线包括固定弱核的全部 mixed cross、宽 cutoff、原补矩、Green、右历史、平台尾及实际复制位置和权；不是 rank-one 局部公式代替弱核。

由(16)，$-\mathbf G^{16}_{\rm base}$ 有严格正的平方幅表示；向任一非负表示加严格正核即可去掉零分量。选16个独立列、固定其余正幅后，极限 Jacobian 的列 $2z_{\alpha i}v_{\alpha i}$ 可逆。非退化零对小 $C^1$ 扰动稳定，所以一个足够大但实际有限的整数 $N$ 给
$$
\boxed{\mathbf G^{16}_N=0.}
\tag{19}
$$
不需要把离散 $1/N$ 假装成光滑 IFT 参数，也不使用无限频率作为最后圆。

(17)保原(11)，因而保全部旧面积、$\mathcal T$、quartic $C$ 与原弱核结构。弱核心不动、强块仍 $W=0$，原 R325(30)、§8 的 $\Psi_+=N(t)C_{22}\sin^2\theta/[6P(t)]$ 使整个 $\Psi=0$ 在允许的每个纤维扰动上准确不变。三条 directed 行及其它 $C^3$ 目标才由(19)同点完整根恢复。前十五行的同点根恢复 R376 的全部已付目标；新增行与(1)–(2)共同给
$$
\boxed{\mathcal Q_{YY,j}(\theta)=0
\quad(j=0,1,2,\ \text{全部 }\theta).}
\tag{20}
$$
同样的正锥可把新增 $\pi/2$ 值设为任一固定有限实数，同时保持旧十五个零；完整第0函数就是该数乘 $\sin^2\theta$。

## 6. 准确范围与继续

本稿在同一个最终全偶真实弱圆上完整支付
$$
\boxed{P^2,\ PW,\ PZ,\ PY,\ ZW,\ W^2,\ ZY,\ WY,\ Y^2.}
$$
此外仍保 $ZZ_0,ZZ_1$。唯一剩余对称函数位置为
$$
\boxed{ZZ_2.}
$$

选择次序与 R376 不变：先固定弱入口、有限观察和实际相对布局，再取同母最大 minor、16形状及全部最终中心，随后静态幅与有限幅盒，最后共同有限 $N$。求根后不再平移或重锚。全体有限 profile 包络确定后，才按 R354 选物理区间、受控 $\omega$ 桥及初始 $h_e$，安装新共同几何；不冒保持旧固定 $g$。

本稿不依赖正在复核的 R358/R365 自然 H 通量表达式或 R371 的具体秩。对称 Gaussian 全部函数还差 $ZZ_2$ 的真实角商及实际值；其余 Gaussian history、canonical 第四 period、同一规范的 joint 条件、同一固定 $g$ 的全时嵌入和 reach 均仍欠，继续按 open 推进。
