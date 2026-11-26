# R621 同场法向协变分块与真实主曲率

2026-11-27。**已证明的完整单元充分界；纯接口尚未科学执行。**
本条直接处理[实际97q连续终态](../notes/2026-11-27-r582-retained-continuous-original-terminal.md)
暴露的环境二阶差损失。它不改原已完成运行，不从宽上界推断真实曲率超标，
也不预告下一候选通过。完整参考全法弦与新全闭面覆盖仍由
[R604](R604-normal-chord-stability-and-finite-parametric-norm-interface.md)要求。

## 1. 输入与法向角差

同一连续径向单元及全部角上，参考圆面
\[
X_0=a_0(s)e_r(\theta)+z_0(s)e_z,\qquad
b_0=\sqrt{(a_0')^2+(z_0')^2}>0,
\quad a_0>0
\]
已经有准确区间jets。当前场为同一材料参数上的
\[
X=a(s)\{e_r+\Pi(T-e_\theta)\}+z(s)e_z,
\quad X_\theta=aT,\quad |T|=1,
\]
其中 `Pi` 是准确连续零均值primitive，且T及所需径向导数的角均值准确为零。
R582的完整反射/半周对称支付这个假设；一般不闭合T不能使用本条。

记差场 `e=X-X0`，原参考正交标架的三个独立协变二阶块为
\[
H_{11}=\frac{e_{ss}-(b_0'/b_0)e_s}{b_0^2},\qquad
H_{12}=\frac{e_{s\theta}-(a_0'/a_0)e_\theta}{a_0b_0},\qquad
H_{22}=\frac{e_{\theta\theta}+(a_0a_0'/b_0^2)e_s}{a_0^2}.
\tag{1}
\]
输入同时有完整一阶差界 `alpha<1`，以及 `|Hij|<=hij`。
这些都指实际同单元、全角连续界，不是请求预算或有限观察。

R604已证两切平面的夹角满足 `sin(angle)<=alpha`，并由alpha<1保证当前浸入。
在每一点选使 `n1 dot n0>0` 的实际法向。置
\[
\boxed{d_n=\alpha\sqrt{\frac{2}{1+\sqrt{1-\alpha^2}}}.}
\tag{2}
\]
由 `|n1-n0|²=2(1-cos(angle))` 及正余弦，准确得到 `|n1-n0|<=dn`。
有理化形式(2)避免近零时相减两个接近1的数。
这里使用同一材料点的两个法向；没有假定一组常法向适用于整条角圈。

## 2. 先分开primitive的水平与竖直分量

沿用原旋转frame的同一三个标量
\[
T-e_\theta=Ae_\theta+Be_r+Ce_z.
\]
它们由原完整u/v与所有所需jets计算；没有切换成另一个截断场。
对j=0,1,2设
\[
u_j=\sup\sqrt{(\partial_s^jA)^2+(\partial_s^jB)^2},\qquad
v_j=\sup|\partial_s^jC|.
\]
均值为零的水平向量与竖直标量分别使用R504的primitive范数 `pi/2<11/7`。
在当前观察角固定参考法向
\[
n_0=n_r e_r+n_z e_z,\quad n_r=-z_0'/b_0,\quad n_z=a_0'/b_0.
\]
于是有完整上界
\[
\boxed{|n_0\cdot\Pi(\partial_s^j(T-e_\theta))|
\le p_j^n:=\frac{11}{7}(|n_r|u_j+|n_z|v_j).}
\tag{3}
\]
证明是在固定观察角将水平primitive与该角的单位er作内积，应用向量值卷积的
同一L1核界，再处理竖直分量；不是把变化的er移进primitive而忽略其导数。
在近帽处参考法向接近竖直时，(3)明确保留很小的水平系数。

## 3. 三个参考法向投影的完整公式

记
\[
\Delta a=a-a_0,\quad\Delta z=z-z_0,\quad
\ell=b_0'/b_0,\quad\omega=a_0'/a_0,\quad
\gamma=a_0a_0'/b_0^2,\quad f=a'-\omega a.
\]
同场差及其两jets可先准确相消再包围；当前/参考相同高度不是可以删除角竖分量C的理由。
由(1)与原旋转frame导数，以下表达式是各投影的上界：
\[
\begin{aligned}
q_{11}=b_0^{-2}\big(&|n_r(\Delta a''-\ell\Delta a')
                    +n_z(\Delta z''-\ell\Delta z')|\\
&+|a''-\ell a'|p_0^n+|2a'-\ell a|p_1^n+|a|p_2^n\big),
\end{aligned}\tag{4}
\]
\[
q_{12}=\frac{|n_r(fB+aB_s)+n_z(fC+aC_s)|}{a_0b_0},
\tag{5}
\]
\[
\begin{aligned}
q_{22}=a_0^{-2}\big(&|n_r\{-\Delta a+a(B_\theta-A)+\gamma\Delta a'\}
                     +n_z\{aC_\theta+\gamma\Delta z'\}|\\
&+|\gamma a'|p_0^n+|\gamma a|p_1^n\big).
\end{aligned}\tag{6}
\]
所有乘积、和、导数及上确界在同一个完整单元取有证包围。
(5)(6)没有将角向框架项遗漏：原H12的e_theta分量、原H22中的
`a(A_theta+B)e_theta` 与该点n0严格正交，故在这个投影中准确为零。
H22的er项仍含 `B_theta-A`，不能删掉A；H11保留所有primitive二阶项。

由定义与(3)--(6)，`|n0 dot Hij|<=qij`。
再由(2)，
\[
\boxed{|n_1\cdot H_{ij}|\le q_{ij}+d_n h_{ij}=:\widehat h_{ij}.}
\tag{7}
\]
这里保留法向转动乘以**完整环境**二阶差的一项；
不能只用参考法向投影而把真实法向当成不动。

## 4. 换到当前实际主曲率与全闭reach

同单元参考两主曲率的绝对值上界为
\[
k_m=\frac{|a_0'z_0''-z_0'a_0''|}{b_0^3},\qquad
k_o=\frac{|z_0'|}{a_0b_0}.
\]
设
\[
c_1=\overline{k_m}+\widehat h_{11},\quad
c_2=\overline{k_o}+\widehat h_{22},\quad b=\widehat h_{12},
\quad \Lambda=\frac{c_1+c_2+\sqrt{(c_1-c_2)^2+4b^2}}2.
\]
则同单元当前场的真实主曲率有界为
\[
\boxed{K_{\rm cell}=\frac{\Lambda}{(1-\alpha)^2}.}\tag{8}
\]

证明：用参考联络计算当前二阶微分后投影n1，换成当前联络只差当前切向量。
参考二阶形式在子午/角圈正交标架中对角化，投影n1只乘一个绝对值≤1的因子。
故任意材料向量 `x1 e1+x2 e2` 的当前二次形式绝对值被
`c1*x1²+2b*|x1*x2|+c2*x2²` 控制。其上界是Lambda乘参考长度平方。
原一阶差界又给当前长度至少 `(1-alpha)` 倍参考长度，得(8)。
没有假定两个形算子共用特征方向，也没有在某个退化坐标量上相除。

完整全闭面每个单元分别求(8)，最后取最大K；原全域delta/alpha仍独立取其真正最大值。
R604可取 `lambda=1+alpha_global,nu=alpha_global` 以及这个**直接实际K**，
继续完整近远法弦条件。参考rho必须已由当前比较面全闭证书支付；
旧候选的reference/范数不得跨q转移。中央柱、两帽、轴和上下镜像全保原明确覆盖，
帽轴采用笛卡尔图。全时间结论仍需要真实相位像恒等式或所有量的全时间统一界。

## 5. 同一遍读取的纯实现

[r621_normal_projected_curvature_20261127.py](../scripts/r621_normal_projected_curvature_20261127.py)
保原R604的C0/C1/协变C2代数，在**同一组**材料和mean区间jets、同一次A/B/C组装中
追加(2)--(8)。原三个独立H块只算一次；没有第二次材料/ODE/mean/角场查询。
它返回原三范数及 `R621_principal_curvature_upper`，并保存各法向块的小范围字段供定位。
所有公式使用已绑定的同一个向外区间后端。

本地仅纸推、AST与源结构核对；没有本地执行数值。
下一实际scope须绑定真实最新保留态、固定原mesh和完整新mean参考，重新声明必要科学成本；
不重放原f1c范围来假装取得新候选进展。即使新曲率界通过，固定g等距、
全时幅度、主README与强目标仍需继续完成。
