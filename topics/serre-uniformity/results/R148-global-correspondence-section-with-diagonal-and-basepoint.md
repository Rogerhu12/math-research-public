# R148：含对角分量的真实对应截面与八百倍高度差

日期：2026-11-12。**状态：已证明。** 本文把 R144 所需的全局截面具体写成真实对应线丛的张量表达式，并证明其对角及基点刚性化、准确的 $800$ 倍率以及碰撞处必须采用的线丛计算规则，并完成 F2 在真实 CM12 点的规范截面坐标。允许对应含有对角分量，因而覆盖 R94 的全部实际方向 $F_n=aT_n+c\operatorname{id}$。

此构造确定要计算的全局截面，不等于已经得到它的局部 Poincaré 高度。尤其不能把对角上张量因子相消为 $1$ 误读成该截面的高度恒为零。

## 1. 同一范数约定和对称线丛

设 $X/k$ 是光滑射影几何连通曲线，$b\in X(k)$，$J=\operatorname{Pic}^0(X)$，$x(P)=[P-b]$。采用 R18、R33、R140 的度零除子范数约定：若 $A,D$ 是相应除子，则
$$\mathcal P_{[A],[D]}=\operatorname{Norm}_{A}\mathcal O_X(D).$$
这正是 [Edixhoven–Lido, §6.3，式(6.3.3)–(6.3.13)](https://doi.org/10.1017/S1474748021000244) 的对称双扩张 $M$。这里先固定这个实际范数约定，不在计算中另换主极化的符号。

令 $\mathscr B$ 是 $X\times X$ 上来自真实对称整对应的线丛，双次数均为 $v$，诱导的 Jacobian 算子为 $F$。假设
$$\operatorname{Tr}(F|H^0(X,\Omega^1))=0.$$
置
$$\mathscr B_b=(\operatorname{id},b)^*\mathscr B,
\qquad K_{\mathscr B}=\Delta^*\mathscr B.$$
对应的 Lefschetz 公式含对角自交，给
$$\deg\mathscr B_b=v,\qquad \deg K_{\mathscr B}=2v.$$
因此
$$\kappa_b=[K_{\mathscr B}\otimes\mathscr B_b^{-2}]\in J(k).\tag{148.1}$$

**交换符号的规范。** 真实对称 Cartier 对应给交换两个变量的线性化。先将它规范到在 $(b,b)$ 的纤维上为恒等。在特征不为二时，原线性化在该纤维上的特征为 $\epsilon\in\{1,-1\}$，将整个线性化乘 $\epsilon$ 即满足要求，且平方仍为恒等。这不改变对应算子 $F$。对于
$$\mathscr B=\mathcal O(aT_n+c\Delta),\quad n>1\text{ 平方自由},$$
自然交换线性化的该特征是 $(-1)^c$：$T_n$ 不含对角分量，故其在对角线的线性化为恒等；对角的法丛交换为负。数值计算可以保留这个明确符号；$47$ 进对数杀掉 $-1$，但精确纤维坐标仍不应隐去它。

## 2. 全局线丛、两处刚性化及真实平移

定义 $X\times X$ 上的实际线丛
$$
\boxed{\mathscr L_{F,b}=
\mathscr B\otimes
\operatorname{pr}_1^*(\mathscr B_b\otimes K_{\mathscr B}^{-1})
\otimes\operatorname{pr}_2^*\mathscr B_b^{-1}.}
\tag{148.2}
$$

### 定理 148.1

线丛 (148.2) 的第一变量次数为零，并具有彼此相容的规范平凡化
$$
(b,\operatorname{id})^*\mathscr L_{F,b}\simeq\mathcal O_X,
\qquad \Delta^*\mathscr L_{F,b}\simeq\mathcal O_X.
\tag{148.3}
$$
以第一式刚性化后，它是普遍度零线丛沿
$$P\longmapsto Fx(P)-\kappa_b$$
的实际拉回。第二式因此给出唯一的全局无零极截面
$$
\sigma_{F,b}(P)\in\mathcal P_{x(P),\,Fx(P)-\kappa_b}^{\times},
\qquad \sigma_{F,b}(b)=1.
\tag{148.4}
$$

**证明。** 第一变量次数是 $v+(v-2v)=0$。对角拉回 (148.2) 的三个因子，得到
$$K_{\mathscr B}\otimes\mathscr B_b\otimes
K_{\mathscr B}^{-1}\otimes\mathscr B_b^{-1}.$$
用线丛及其对偶的评价同构相消，得到第二个平凡化，过程中没有选择一个有理函数或点值。

在 $b\times X$ 上，规范对称同构将第一个因子识别为 $\mathscr B_b$。第二个因子成为固定一维空间
$$\mathscr B_b(b)\otimes K_{\mathscr B}(b)^{-1}.$$
两条拉回路径都在 $(b,b)$ 取值，因此这两个固定纤维规范相同，评价同构将其识别为 $k$。再与第三个因子 $\mathscr B_b^{-1}$ 相消，得到第一个平凡化。第1节已将交换同构在 $(b,b)$ 规范为恒等，所以两种平凡化在交点相容。

固定第二变量 $P$，(148.2) 的 Picard 类是
$$
[(\operatorname{id},P)^*\mathscr B]+[\mathscr B_b]-[K_{\mathscr B}].
$$
按实际对应的定义，
$$[(\operatorname{id},P)^*\mathscr B]-[\mathscr B_b]=F[P-b].$$
于是该类准确为 $Fx(P)-\kappa_b$。已经给定 $b$ 处刚性化的度零线丛的普遍性质，给出实际线丛同构，且在任意基变换下相容；不是仅有 Picard 类相等。

按同一个范数约定，对 $P-b$ 取范数就是取该线丛在 $P$ 与 $b$ 的纤维之商：
$$\mathcal P_{x(P),Fx(P)-\kappa_b}
\simeq\mathscr L_{F,b}(P,P)\otimes\mathscr L_{F,b}(b,P)^{-1}.$$
两处规范平凡化给元素 $1\otimes1^{-1}$，即 (148.4)。它处处无零极、在 $b$ 为零纤维的单位。任意两个这样的全局截面之比是完整几何连通曲线上的常数，在 $b$ 为 $1$，故二者相同。证毕。

这同时从头证明本题需要的 Edixhoven–Lido §7 对应截面构造的实例，包括其对角分量；没有引用未发表算法中“对应不含对角”的额外假设。

## 3. 从全部尖点的规范准确转回基点规范

现取本题全部尖点之和 $D$、$d=\deg D$、$U_b=[db-D]$，并假设真实对应满足
$$F(D)=vD.$$
这是 R33、R94 已识别的实际尖点除子恒等式。用 R33 的实际代表
$$\eta_{D,F}=[dK_{\mathscr B}-2vD],$$
有精确的 Jacobian 点恒等式
$$
\boxed{\eta_{D,F}=d\kappa_b+2FU_b.}
\tag{148.5}
$$

**证明。** 对实际度零除子 $db-D$ 施加对应，得到
$$FU_b=[d\mathscr B_b-vD].$$
所以右边等于
$$[dK_{\mathscr B}-2d\mathscr B_b]
 +[2d\mathscr B_b-2vD]
=[dK_{\mathscr B}-2vD].$$
证明用的是实际对应和实际线丛，并未仅比较 $J(k)\otimes\mathbb Q$ 的坐标，故不遗留一个未知挠点平移。证毕。

R54 使用 $G=2F$、$\eta_{D,G}=2\eta_{D,F}$。R144§5.1 给出的基点转换是
$$G_b=2d^2F,\qquad \eta_b=d\eta_{D,G}-4dFU_b.$$
将 (148.5) 代入，即得
$$
\boxed{G_b=2d^2F,\qquad\eta_b=2d^2\kappa_b.}
\tag{148.6}
$$
因而 R144 的整条曲线上的归一化截面准确为
$$\boxed{t_b=\sigma_{F,b}^{\otimes 2d^2}.}\tag{148.7}$$
这里两边通过真实双扩张群律识别。它们在同一线丛上都是全局无零极截面，且在 $b$ 为 $1$；第2节的唯一性排除了额外常数。对同一个相容 Poincaré 对数，遂有
$$
\boxed{\lambda(t(P))-\lambda(t(b))
=2d^2\lambda(\sigma_{F,b}(P)).}
\tag{148.8}
$$
左边可用 R144 的任意同一全局代数平凡化 $t$；常数已在差值中消去。

## 4. 层41的准确倍率及全部54条右端

在层41取 $b=P_{-3}$、$d=20$。于是
$$2d^2=800\equiv1\pmod{47},\qquad
800^{-1}\equiv2921709\pmod{47^4}.$$
R144 的54条右端可以改写为
$$
L_{{\rm rel},n}=800\lambda_{47}(\sigma_{F_n,b}(P_{-12}))
-\log_{47}(41)b_3(F_n),\quad n\in\mathcal I\setminus\{1\},
\tag{148.9}
$$
以及
$$L_{{\rm rel},54}=800\lambda_{47}(\sigma_{F_2,b}(P_{-7})).\tag{148.10}$$
因此无需分别计算一个任意归一化截面在 $b$ 的绝对值。准确的 $800$ 倍不可漏掉；它在47处为单位，所以不增加精度损失。R144 的矩阵、坏分量和同一有限靶均保持原规范。

对实际方向 $F_n=aT_n+c\operatorname{id}$，用任意非零有理微分 $\omega$ 的典范除子 $K_\omega=\operatorname{div}\omega$，可取
$$
\mathscr B_b=\mathcal O(aT_n(b)+cb),\qquad
K_{\mathscr B}=\mathcal O(aQ_n-cK_\omega),
\quad Q_n=\Delta^*T_n.
\tag{148.11}
$$
其中第二式的 $-cK_\omega$ 来自
$$\mathcal O(\Delta)|_\Delta\simeq T_X\simeq\Omega_X^{-1};$$
绝不能将含 $\Delta$ 的对应当成不含 $\Delta$，再把一个“对角点值”代入有限乘积。

例如 $F_2=27T_2+4$，R144 的真实关系 $T_2b=3P_{-12}$ 给
$$v=85,\qquad \mathscr B_b=\mathcal O(81P_{-12}+4b),$$
$$K_{\mathscr B}=\mathcal O(27Q_2-4K_\omega),\qquad \deg Q_2=22.$$
故
$$
\kappa_b=[27Q_2-4K_\omega-162P_{-12}-8b].
\tag{148.12}
$$
其次数是 $27\cdot22-4\cdot106-162-8=0$。特别，$P_{-12}$ 在基点修正中的重数为 $81$，不是 $27$；粗模点上合并的三条二同源仍须按三重计数。

## 5. 碰撞处如何计算，及为什么不产生未知常数

公式 (148.2) 是线丛恒等式，(148.3) 是线丛与对偶的评价；二者都不要求一个相交除子的有理截面在该点非零。若计算只保存了方程的点值而丢掉局部线丛生成元，就无法在碰撞处实施这些同构。

具体地，在曲线乘积的一个开集上，若某实际 Cartier 对应由局部方程 $f$ 定义，则 $e=f^{-1}$ 是 $\mathcal O(Z)$ 的局部生成元；规范有理截面 $1$ 在这个生成元下的系数是 $f$。即使 $f$ 在交点为零，$e$ 仍然是线丛的生成元。拉回线丛时先拉回生成元及其变换规律，再在同一纤维中将因子与对偶相消，不能先对 $f$ 取零值后做数值除法。

若另一开集使用方程 $f'=uf$，$u$ 为单位，则生成元改变为 $e'=u^{-1}e$。各条轴和对角线都拉回**同一个**单位 $u$；在 (148.3) 中它们准确抵消。因此算法保留这些实际单位，就得到同一个全局截面，局部选择不会引入一个待拟合的点依赖函数。

对角分量需另用伴随公式。若 $t$ 是局部参数，选 $t_2-t_1$ 为对角方程，则
$$I_\Delta/I_\Delta^2\simeq\Omega_X,\quad
t_2-t_1\longmapsto dt.$$
对偶后，$\mathcal O(\Delta)|_\Delta$ 的相应生成元对应 $\partial/\partial t$。若 $\omega=w(t)dt$，其有理代表是 $\omega^{-1}=w(t)^{-1}\partial/\partial t$。故必须保留 $w(t)$ 及其在新参数下的变换；R123 的真实 Kodaira–Spencer 尺度和 R110 的实际典范截面提供这项输入。若 $w$ 有零极，则先保留其阶和单位部分，不能只取剩余值。

此外，将两个线性等价除子换成不交代表时，仍须沿实际主函数应用范数同构；R141、R145、正在进行的 Miller 链中出现的这些范数不会因 (148.3) 而消失。全局截面在 (148.3) 的乘积框架中坐标是 $1$，在计算局部对数的 Poincaré 框架中一般有非平凡坐标。

### 5.1 F2 在真实 CM12 点的规范截面坐标

记 $b=P_{-3}$、$u=P_{-12}$，取 R147 的准确局部参数 $x=j$（在 $b$）及 $w=j-54000$（在 $u$）。固定 R110 的真实典范微分
$$\omega=a_b(x)dx\quad\text{在 }b,\qquad
\omega=a_u(w)dw\quad\text{在 }u.$$
两点的系数均为47进单位。记
$$
c=\partial_X\Phi_2(0,54000)=6549518250000,\qquad
\rho=a_b(0)/a_u(0).
$$
R147 已证明 $c\equiv652438$、$\rho\equiv1525119\bmod47^4$。

在 $F=27T_2+4\,\mathrm{id}$ 和 R148 的同一范数、交换线性化规范下，置
$$
D_F(u)=27(T_2u+3u-Q_2)+4(u+b+K_\omega).
\tag{148.13}
$$
其次数为
$$
27(3+3-22)+4(1+1+106)=27(-16)+4(108)=0.
$$
在 $b,u$ 的局部阶分别为31和85。这里 $Q_2$ 与这两个圆盘均不相交：R147 的整数方程给
$$
\Phi_2(0,0)\equiv27,\qquad
\Phi_2(54000,54000)\equiv30\pmod{47},
$$
所以甚至忘掉 Cartan 结构后都没有相应二阶自同源；$K_\omega$ 也因两个微分系数为单位而避开这两个圆盘。

用 $\mathscr B_b^{-1}(u)$ 这个固定纤维在度零范数中相消，R148 的 Poincaré 纤维准确识别为
$$
\mathcal P_{[u-b],\,F[u-b]-\kappa_b}
=\operatorname{Norm}_{u-b}\mathcal O_X(D_F(u)).
$$
右边选择明确局部生成元
$$
e_b=x^{-31},\qquad e_u=w^{-85},\qquad
e_{\rm N}=e_u\otimes e_b^{-1}.
$$
这里使用 $K_\omega=\operatorname{div}\omega$ 的实际除子模型；它在两点局部为零，生成元为1。该选择确定范数纤维中的一个非零元素，而不是一个预先规定其高度为零的解析框架。

**准确坐标公式为**
$$
\boxed{
\sigma_{F,b}(u)=c^{27}\rho^4\,e_{\rm N}.
}
\tag{148.14}
$$

#### 逐生成元证明

先在张量因子层面分别计算 $T_2$ 和 $\Delta$。它们各自第一变量的次数为 $-16$、$108$，所以这里仅是 Deligne 范数线的计算；只有加权和 $27T_2+4\Delta$ 才有次数零并代表上述 Poincaré 纤维。

##### T2 因子

R147 在 $(b,u)$ 的实际共同局部方程是
$$
f(x,w)=\Phi_2(x,54000+w),\quad
f(0,w)=w^3,\quad f(x,0)=xg(x),\quad g(0)=c.
$$
以 $f^{-1}$ 作为 $\mathcal O(T_2)$ 的环境线丛生成元。其在 $b\times X$ 的拉回是 $w^{-3}$；在 $X\times u$ 的拉回是 $(xg(x))^{-1}$。两个拉回使用同一个环境生成元，所以没有另外的比例常数。

固定第二变量为 $u$ 后，因子
$$
\mathcal O(T_2u+3u-Q_2)\otimes\mathcal O(-3u)|_u
$$
的第一部分在 $b,u$ 的标准生成元分别为 $x^{-1}$ 和 $w^{-3}$；固定纤维选择 $w^3$。对 $b$ 处的基点刚性化，$(xg(x))^{-1}\otimes w^3$ 的像是1，所以 $x^{-1}\otimes w^3$ 的像是 $c$。对 $u$ 处的对角刚性化，$w^{-3}\otimes w^3$ 的像是1：$\mathcal O(T_2)$ 与其对角拉回的因子在这里通过实际评价同构相消。

因此标准范数生成元的像是 $1/c$，规范单位截面在该生成元中的坐标是 $c$。

##### 对角因子

采用 R148 的对角方程 $t_2-t_1$，伴随同构将其逆的对角限制送到 $\partial/\partial t$。自然交换在该纤维上为负，故规范交换同构是自然交换乘以 $-1$。

固定第二变量为 $u$，对角因子的第一变量除子是 $u+b+K_\omega$。其标准局部生成元在 $b,u$ 分别为 $x^{-1}$、$w^{-1}$。逐项保留伴随尺度后：

- 在 $b$，$\mathcal O(b)$ 的环境拉回生成元为 $-x^{-1}$，而 $K_{\mathscr B}^{-1}=\Omega_X$ 的除子代表把1送到 $\omega=a_b(x)dx$。规范交换多出的负号与 $-x^{-1}$ 相消，故标准生成元的基点刚性化值为 $a_b(0)$。
- 在 $u$，固定第二变量的对角生成元是 $-w^{-1}$，其对角伴随限制是 $\partial/\partial w$。相应标准生成元的对角刚性化值为 $-a_u(0)$。

于是标准范数生成元的像是 $-a_u(0)/a_b(0)$，规范单位截面的坐标是 $-\rho$。这一步必须保留两点真正微分的尺度，不能改用未作粗模修正的权二数值比。

张量乘以27和4后，得到 $c^{27}(-\rho)^4=c^{27}\rho^4$，局部阶也相加为31和85，即证 (148.14)。

#### 模47⁴的完整数值

在上面明确的范数生成元中，
$$
\boxed{
\sigma_{F,b}(u)\text{ 的坐标 }=3987767\pmod{47^4}.
}
\tag{148.15}
$$
R148 的800次幂后，坐标为
$$
\boxed{3987767^{800}=4053094\pmod{47^4}.}
\tag{148.16}
$$
仅对这两个单位坐标取47进对数，分别为
$$
3840276,\qquad2901451\pmod{47^4},
$$
且第二个准确等于第一个乘800。

**这些对数不是最终高度。** 对同一个真实 Poincaré 对数，还须加入明确范数生成元 $e_{\rm N}$ 的值：
$$
\lambda_{47}(\sigma_{F,b}(u))
=3840276+\lambda_{47}(e_{\rm N})\pmod{47^4}.
\tag{148.17}
$$
R141、R145 的解析框架一般不等于此处 $e_{\rm N}$；二者之间仍需实际除子搬运和范数。这里已经确定的是全局规范代数截面的实际纤维元素，而没有把尚待求的框架高度设为零。

脚本 p41_cm12_global_fibre47.py 从 R147 的尺度小证书重建全部数值，纯标准库准确整数运算；输出 p41_cm12_global_fibre47_certificate.json。运行方式：

~~~
python -B scripts/p41_cm12_global_fibre47.py \
  --input scripts/data/p41_cm12_scales47_certificate.json \
  --output /tmp/p41_cm12_global_fibre47_certificate.json
~~~

### 5.2 F2 在真实 CM−7 点的规范截面坐标

沿用本篇的 $b=P_{-3}$、$u=P_{-12}$，现在记 $c_7=P_{-7}$，$z=j+3375$ 是它的局部参数。固定同一个 R110 典范微分
$$\omega=a_b(x)dx\quad\text{在 }b,\qquad
\omega=a_7(z)dz\quad\text{在 }c_7,$$
其中 $x=j$。

#### 真正的 CM 点和微分尺度

在短模型
$$E:y^2=x^3-35x-98,\qquad j(E)=-3375$$
上实际生成41挠点，并把 Weil 配对校准到 R102 的固定根。取 $s^2=-7$、$r=(-7+s)/2$、$\alpha=(1+s)/2$。以 $r$ 为二阶核的规范 Vélu 商，随后按 $(x',y')\mapsto(x'/\alpha^2,y'/\alpha^3)$ 返回原曲线，得到真正的 CM 自同源。

实际挠点矩阵和 Frobenius 矩阵分别为
$$U=\begin{pmatrix}8&23\\26&34\end{pmatrix},\qquad
F=\begin{pmatrix}0&9\\13&0\end{pmatrix}\pmod{41}.$$
满足 $U^2-U+2=0$、$FU=(1-U)F$。它固定的唯一非分裂项链是 R102 第412条。由 R79 的实际固定点识别，该点就是全局有理的 $P_{-7}$。

生成器计算全部73个权二坐标以及族 $y^2=x^3-35x-98+t$ 的一阶展开。独立复核以椭圆群律重建 CM 自同源，验证完整41挠点、原 Weil 根、项链、Frobenius，并改用另一权一实现和直接迹重算全部 $2\times73$ 个系数；全部通过。小证书 p41_cm7_q2_support47_verified.json.gz 的 SHA256 为 a6c1733d5f852556e62d9ca901412fb6a786529ddae0726ef5d9eab07f24aa74。

对任意 $A B\ne0$ 的短模型，由 R123 的准确公式以及
$$j=\frac{6912A^3}{4A^3+27B^2}$$
直接微分可得
$$
\frac{\beta}{dj}=\frac{4A^3+27B^2}{124416A^2B}.
$$
在当前曲线，它恰为 $-1/170100$。固定典范截面的实际权二值是143613，故
$$
\boxed{
a_7(0)=2865069,\qquad
a_b(0)/a_7(0)=2314740\pmod{47^4}.
}
$$
两者均为47进单位；没有用形式坐标导数代替真实微分。

#### 两条真实自同源分支的碰撞单位

在 $(c_7,c_7)$ 附近，令两变量的局部参数为 $z_1,z_2$。R79 已识别两个不同的二阶 CM 核，它们都保留唯一的 CM 项链；第三个核的目标不在该点。由于这里没有额外椭圆自同构，源、靶 $j$ 都是实际粗模参数。因此实际 Cartan 对应的这个完成局部除子正由
$$f(z_1,z_2)=\Phi_2(-3375+z_1,-3375+z_2)$$
定义，至多相差一个单位。

整数多项式准确展开为
$$
f(z,0)=z^2(z-16584750),
$$
$$
f(z,z)=z^2(-58046625+16478z-z^2).
$$
两处二阶首系数模47分别为46、20，都是单位。故 $\mathcal O(T_2)|_{X\times c_7}$ 与对角拉回在此各有阶二，其相消留下准确单位
$$
\boxed{
\eta_7=\frac{-58046625}{-16584750}=\frac72.
}
$$
如果更换实际 Cartier 方程 $f$ 为 $vf$，两个首系数同时乘 $v(0,0)$，因此该比不变。这是线丛生成元的限制之比，未对两个零值作数值除法。

#### 完整 F2 范数纤维

固定
$$
D_F(c_7)=27(T_2c_7+3u-Q_2)+4(c_7+b+K_\omega).
$$
在 $c_7$，$T_2c_7$ 的两个自同源支点与 $Q_2$ 的二重支点准确相消；在 $b$，两者均不经过。故 $D_F(c_7)$ 在 $b,c_7$ 的局部阶都为4。用
$$
e_{\rm N}=z^{-4}\otimes(x^{-4})^{-1}
$$
作为 $\operatorname{Norm}_{c_7-b}\mathcal O(D_F(c_7))$ 的明确生成元。

$T_2$ 因子的基点刚性化值为1；对角刚性化中，标准生成元的值是竖直首单位除以对角首单位。因此规范截面坐标是 $\eta_7=7/2$。对角线因子沿用 R148 中经规范的交换符号，坐标为 $-a_b(0)/a_7(0)$。两个单因子各自是非零度的范数因子；只有 $27T_2+4\Delta$ 的总次数为零。

由此得到真正的全局截面纤维坐标
$$
\boxed{
\sigma_{F,b}(c_7)
=\left(\frac72\right)^{27}
\left(\frac{a_b(0)}{a_7(0)}\right)^4 e_{\rm N}
=4622835\,e_{\rm N}\pmod{47^4}.
}
$$
其800次幂坐标为4776552；这两个坐标的47进对数分别为3608895和3224529模47⁴。完整规范负号因第四次幂相消，未被任意丢弃。

最后仍须保留
$$
\lambda_{47}(\sigma_{F,b}(c_7))
=\log_{47}(4622835)+\lambda_{47}(e_{\rm N}).
$$
本节完成的是全局规范截面在实际范数纤维中的坐标，未把框架高度设为零。

#### 证书

p41_cm7_global_fibre47.py 仅使用已独立验证的 CM7 证书、R147 的基点尺度证书及 R110 典范数据，以准确有限算术重建全部整数多项式和微分数值。输出 p41_cm7_global_fibre47_certificate.json 为1587字节，SHA256 为38215586c7df441b9860d321f2f13221c6c5ac532dc49337b86b1c1fad90abfc。

~~~
python -B scripts/p41_cm7_global_fibre47.py --script-dir scripts \
  --input scripts/data/p41_cm7_q2_support47_verified.json.gz \
  --base-scales scripts/data/p41_cm12_scales47_certificate.json \
  --output /tmp/p41_cm7_global_fibre47_certificate.json
~~~

## 6. 积分形式与当前完成边界

以上构造也在好约化 DVR 上成立：使用光滑曲线模型及实际对应的 Cartier 闭包，所有拉回、对偶和评价都定义在整模型上。对于层41的辅助素数47，曲线及其乘积正则，纯水平对应的 Weil 除子因此为 Cartier；对角的伴随同构也整地成立。即使方向含 $T_{47}$，这里不需要把其特殊纤维假定为 étale。

所以实际整数方向的 (148.3) 不需要除以47。更换为有理方向时，应先取固定的清分母张量幂；这和将任意分析框架当成全局代数截面不同。

本结果完成了 R144 对全局截面的**明确代数选择**，并给出接入现有范数、典范微分及碰撞计算的准确规则。剩余工作是将各个真实对应、纤维代表和局部单位实际算入同一 Poincaré 框架，得到 (148.9)–(148.10) 的54个数，再求完整 QC 函数和全部圆盘的共同根。本文不以全局平凡化的存在或形式写法宣称这些数值和根分类已经完成。

## 来源

- [R18](R18-norm-rigidification-interface.md)、[R33](R33-hecke-norm-and-component-data.md)：同一实际度零范数、尖点规范和真实对应平移。
- [R94](R94-central-involution-and-complete-Chow-Heegner-operator.md)：全部实际整数方向、固定除子及对角典范项。
- [R144](R144-cm-height-difference-calibration-without-section-constants.md)：准确基点转换、相对高度及可逆校准。
- B. Edixhoven、G. Lido，*Geometric quadratic Chabauty*，Journal of the Institute of Mathematics of Jussieu，§§6.3、6.4、7，尤其命题7.2、7.5、7.8，[正式出版全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9DFF959E23514A586DA27E3F165A79ED/S1474748021000244a.pdf/geometric_quadratic_chabauty.pdf)。本篇所需的线丛表达式、平移、倍率和碰撞规则均在正文直接证明。
