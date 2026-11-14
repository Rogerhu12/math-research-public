# R426 — 原 degree18 的两条唯一 CM7 线、完整二挠作用与负权单位输入

日期：2026-11-14。**状态：已证明。** R424 实际交替核中的两条 degree18 来源满足
\[
\mathscr M_\gamma F_{18}=\omega\gamma F_{18},\qquad
\mathscr M_\gamma G_{18}=\omega^2\gamma G_{18}.
\]
它们分别是整个对应 CM 型块中的唯一特征线，还构成完整二挠平移的真实二维空间；任一非零二挠平移在该空间上的行列式准确为 \(-1\)。

同一普通 ray 上它们的完整 core 都是 \(-\lambda\)，且对每个当前素数
\[
\int_{\mathbf Z_p^\times}x^{-(p-5)}\,d\nu_{F_{18}}\in\mathcal O^\times .
\]
这是原交替核中的实际负矩。没有从辅助来源质量、单一 CM7 特征或有限纤维计算给另一条曲线赋 rank-two 身份。

## 1. 同一个实际来源与 trace 规范

保持原 \(E_b:y^2=x^3+b\)、\(b=17\)、同一 sigma、普通周期
\(\Omega=\Omega_p\) 和 R410 ray。置
\[
\delta^2=-3,\quad\omega=(-1+\delta)/2,\quad
\gamma=(5+\delta)/2=3+\omega,\quad N\gamma=7,
\]
\[
P_2(X)=X^2-\frac{4b}{7}X+\frac{16b^2}{7},\qquad X=x^3,
\]
\[
f_b(x)=xP_2(x^3),\qquad
g_b(x)=x^9-30bx^6-144b^2x^3-32b^3.
\]
R424 的两条实际来源为
\[
\boxed{F_{18}=\sigma^{18}f_b(x),\qquad G_{18}=\sigma^{18}g_b(x).}
\tag{1}
\]
它们在完整 \(\mathcal S_{18}=\sigma^{18}L(18O)\) 中整，且
\[
F_{18}=z^4+O(z^{10}),\qquad G_{18}=1+O(z^6).
\tag{2}
\]
CM 型分别为 \(4,0\bmod6\)。原算子规范是
\[
\mathscr M_a(\sigma^N f)=\sigma^N\operatorname{Tr}_{[a]}
\left[(r_{\bar a}/r_a)^Nf\circ[\bar a]\right],
\qquad r_a=\sigma(az)/\sigma(z)^{Na}.
\tag{3}
\]
没有额外选择不定根单位。

## 2. 完整 CM7 身份的特征零证明

准确有
\[
\boxed{\mathscr M_\gamma F_{18}=\omega\gamma F_{18},\qquad
\mathscr M_\gamma G_{18}=\omega^2\gamma G_{18}.}
\tag{4}
\]
以下给有限而完整的原 division-trace 证明。

先取 \(b=1\)，记
\[
r=(2-6\delta)/7,\quad\bar r=(2+6\delta)/7,\quad
q(u)=u^3-r,\quad\bar q(u)=u^3-\bar r,
\]
\[
N_{\bar\gamma}(u)=u^6+(28\bar r+12)u^3+(7\bar r+24)\bar r.
\]
原公式为
\[
x(\bar\gamma z)=\frac{xN_{\bar\gamma}(x)}
{\bar\gamma^2\bar q(x)^2}.
\tag{5}
\]
在完整七点纤维 \(x(\gamma z)=a\) 上，坐标代数是
\[
\begin{aligned}
P_a(u)={}&u^7-\gamma^2a u^6+(28r+12)u^4
+2\gamma^2ar u^3\\
&+(7r+24)ru-\gamma^2ar^2.
\end{aligned}
\tag{6}
\]
因此 (3) 除去 \(\sigma^{18}\) 后准确为
\[
\operatorname{Tr}_{\mathbf Q(\delta)[u]/(P_a)}
\left[
\left(\frac{\bar\gamma\bar q(u)}{\gamma q(u)}\right)^{18}
h\left(\frac{uN_{\bar\gamma}(u)}
{\bar\gamma^2\bar q(u)^2}\right)
\right],
\qquad h=f_1\text{ 或 }g_1.
\tag{7}
\]
全部运算在 \(\mathbf Q(\delta)\) 中完成。

完整 theta trace 保 degree18 和 CM 型。型零的完整空间是
\(\sigma^{18}\langle1,X,X^2,X^3\rangle\)，
型四的完整空间是
\(\sigma^{18}x\langle1,X,X^2\rangle\)。
所以四个和三个互异 \(a^3\) 分别足以确定整条来源。

在 \(a=1,2,3,4\) 上，(7) 对 \(g_1\) 的准确输出是
\[
\frac{205}{2}(1+3\delta),\quad1296(1+3\delta),\quad
\frac{6107}{2}(1+3\delta),\quad-65008(1+3\delta).
\tag{8}
\]
这恰为 \(\omega^2\gamma g_1(a)\)，其中
\(\omega^2\gamma=(-1-3\delta)/2\)。
对 \(f_1\)，在 \(a=1,2,3\) 上准确输出为
\[
(-2+\delta)\left(\frac{19}{7},\frac{864}{7},\frac{15033}{7}\right),
\tag{9}
\]
恰为 \(\omega\gamma f_1(a)\)。
这些是完整七维代数迹，不是只选一个逆像或浮点拟合。

若 \(u^6=b\)，同源缩放给
\[
F_{18,b}(z)=u^{-4}F_{18,1}(uz),\qquad
G_{18,b}(z)=G_{18,1}(uz).
\]
(3) 与之交换，故 (4) 对原 \(b=17\) 成立。最终身份只含 (1) 的
有理 \(b\) 系数，没有未定六次根常数。

## 3. 两条线在整个对应型块中唯一

置 \(N_\gamma=\mathscr M_\gamma/(\omega\gamma)\)。
在好约化 \(1009\)、\(\delta=260\)、\(\omega=634\) 中，
对完整型零基 \(\sigma^{18}(1,X,X^2,X^3)\)，同一 (7) 给
\[
N_\gamma=
\begin{pmatrix}
584&774&683&185\\
586&146&260&676\\
241&54&863&160\\
679&224&594&799
\end{pmatrix}\pmod{1009}.
\tag{10}
\]
\(N_\gamma-\omega I\) 的左上三阶子式为 \(899\ne0\)。
所以特征零中的核至多一维；(4) 的实际 \(G_{18}\ne0\) 使它恰为一维。

对完整型四基 \(\sigma^{18}x(1,X,X^2)\)，准确矩阵为
\[
N_\gamma=
\begin{pmatrix}
521&260&978\\
948&146&943\\
815&73&342
\end{pmatrix}\pmod{1009}.
\tag{11}
\]
\(N_\gamma-I\) 的左上二阶子式为 \(450\ne0\)。
故 \(F_{18}\) 也张成其整个型块的唯一对应特征线。
有限约化仅用于固定特征零线性代数的秩界，不是目标素数扫描。

脚本 scripts/check-r426-degree18-only.js 独立核定 (7)–(11)；
全部七个特征零纤维、两个完整有限域矩阵及两个子式均通过。
该短证书不运行尚待完成的 degree72 四幂计算。

## 4. 完整二挠二维作用及绝对行列式

采用 R416 的规范 lift
\[
T_t^{(18)}F(z)=e^{-18\eta_t(z+t/2)}F(z+t).
\]
对非零 \(t\in E[2]\)，令
\[
e=x(t),\quad e^3=-b,\qquad c_t=e^{-\eta_t t/2}\sigma(t).
\]
原 sigma 加法及完整半周期定标为
\[
c_t^4=(3e^2)^{-1},\qquad
x(z+t)=e\frac{x(z)+2e}{x(z)-e}.
\tag{12}
\]
直接代入 (1) 得
\[
\boxed{
\begin{aligned}
T_tF_{18}
&=c_t^{18}\left(81e^9F_{18}+\frac{27}{7}e^7G_{18}\right),\\
T_tG_{18}
&=c_t^{18}\left(3402e^{11}F_{18}-81e^9G_{18}\right).
\end{aligned}}
\tag{13}
\]
完整多项式验证可先取 \(x=eu,b=-e^3\)。这化成
\[
(u-1)^9f_{-1}\left(\frac{u+2}{u-1}\right)
=81f_{-1}(u)+\frac{27}{7}g_{-1}(u),
\]
\[
(u-1)^9g_{-1}\left(\frac{u+2}{u-1}\right)
=3402f_{-1}(u)-81g_{-1}(u).
\tag{14}
\]
所以没有只按低阶 jet 猜测二维闭包。

按列写 (13)，行列式为
\[
c_t^{36}\{-81^2-3402(27/7)\}e^{18}
=-(3e^2)^{-9}3^9e^{18}=-1.
\tag{15}
\]
矩阵的迹为零、平方为一。当前 \(p>19\) 中所有显示系数整，
行列式为单位。特别同一真实交替核
\[
G_{18}(y)F_{18}(v)-F_{18}(y)G_{18}(v)
\]
在两个输入同时作任一非零二挠平移时准确乘 \(-1\)。
这是完整联合身份，可供新的 degree52 总和核使用。

## 5. 同一 ray 上的完整普通 core

仍用 R413/R420 的
\[
\lambda=-\bar\pi_0^{-1},\qquad \kappa=p/\bar\pi_0^2.
\]
原 ratio 在 \(2\cdot18=36\) 上为
\[
\pi_0/\bar\pi_0\equiv19=1+18\pmod{36}.
\]
原含中心恒等式使整个 \(\mathcal S_{18}\) 上的核为标量。
实际锚 \(\Theta(3z)\) 的原 core 为
\(\bar\pi_0^{-1}=-\lambda\)，因为 \(3\) 在当前普通处为单位。
因此保全部 tame 的完整测度式为
\[
\boxed{
\nu_{F_{18}}|_{p\mathbf Z_p}
=-\lambda[\kappa]_*\nu_{F_{18}},\qquad
\nu_{G_{18}}|_{p\mathbf Z_p}
=-\lambda[\kappa]_*\nu_{G_{18}}.
}
\tag{16}
\]
这使用原 ratio 与真实锚，不是由一个 CM7 特征推所有普通素数的核。

完整 principal 单位质量为
\[
J_{G_{18},0}(0)=1+\lambda.
\tag{17}
\]
R410 已付它为单位。所以 \(G_{18}\) 的 principal Mellin 函数是整
Tate 单位：其余系数模 \(p\) 为零，常数为 (17) 的单位。
\(F_{18}\) 的 principal Mellin 函数则因型四准确为零；不能把
其非主型值当作 principal 中央非零。

## 6. 每个当前素数的一个明确移动负矩单位

由 (2) 和同一原 Amice 规范，
\[
\mu_4(F_{18})=\int x^4\,d\nu_{F_{18}}=24\Omega^4.
\]
(16) 给完整单位正矩
\[
\int_{\mathbf Z_p^\times}x^4\,d\nu_{F_{18}}
=24\Omega^4(1+\lambda\kappa^4)\in\mathcal O^\times.
\tag{18}
\]
对单位 \(x\)，Fermat 同余给
\(x^{-(p-5)}\equiv x^4\bmod p\)。所以
\[
\boxed{
I^F_{-(p-5)}
:=\int_{\mathbf Z_p^\times}x^{-(p-5)}\,d\nu_{F_{18}}
\equiv24\Omega^4(1+\lambda\kappa^4)\not\equiv0\pmod p .
}
\tag{19}
\]
这对每个当前普通 \(p>19\) 成立，使用的是同一原 \(F_{18}\)。
该负权的 tame 型是 \(4\bmod p-1\)，与 (18) 相同；
这个 tame 分支的整 Mellin 函数本身也是单位。

(19) 不证明固定 \(I^F_{-2}\) 为单位：
当 \(p>7\) 时，\(-2\bmod p-1\) 与 \(4\bmod p-1\) 不同。
它也不直接赋值给原 \(J'_S(0)\)。
但在原共享
\[
G_{16}(y)=\sigma(2y)\sigma(2\delta y)/(4\delta)
\]
的 norm-three 深度展开中，取 log 指数 \(p-5=2+6(p-7)/6\)，
(19) 已支付实际单位输入。第一交替分支的 \(G_{18}\) 质量为一，
另一分支的 \(F_{18}\) 质量为零；后续须保同一总和输出和全部补域。

## 7. 与原目标的准确范围

实际原因子为
\[
F_{18}
=\frac{\sigma(z)\sigma(\delta z)\sigma(\gamma z)
\sigma(\bar\gamma z)}{7\delta},\qquad S=G_{16}F_{18}.
\tag{20}
\]
故没有替换 R339 的原六 sigma 目标。
R424/R430 的实际交替来源、条件中央返回及卷积除法可直接使用
(13)、(16)、(19)，但仍须逐个运输共享 sigma 的隐藏深度条件。

新总和 \(S B_{38}\) 的 degree72 CM7 四分量已由本地完整
四幂特征零证书核定，完整证明、真实质量及全部尺度项见
[R436](R436-original-u72-complete-cm7-spectrum-and-exact-masses.md)。
不能因为 \(B_{38},L\) 的 degree38 core 相同就将其乘 \(S\) 后赋成
原 \(T=SL\) 的同一总和 core。总质量零也不允许删掉各谱分量的
尺度质量项。

直接依赖：R398 的原 CM7 division trace；R416 的规范半周期常数；
R424 的实际 \(F_{18},G_{18}\)；R410 的固定 ray 单位结果。
新增的唯一 CM7 线、完整二挠二维作用、degree18 普通锚及移动负矩
单位式均在本文证明。

