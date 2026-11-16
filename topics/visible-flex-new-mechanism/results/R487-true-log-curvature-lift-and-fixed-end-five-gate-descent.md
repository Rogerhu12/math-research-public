# R487 — 五门控制的真实 log 曲率提升、固定端有限修正与预选模型的边界

本稿纯纸面，不执行程序、积分、优化、秩、profile、开发或旧检查。它消费
[R481](R481-polynomial-flat-tail-regularity-for-all-five-cap-conditions.md)
的五门真实满秩，说明它怎样进入原 \(\rho=v''>0\) 参数化。它不声称新
cap5 搜索的十五条预选列自动满秩，也不声称一个有界搜索的驻点就是
允许 cap 类的驻点。

## 1. 完整对象和变动域

采用 R471/R475 的允许 cap \(U(t)\)，\(\ell<t\le0\)，记
\[
 p=U'>0,\quad r=U''>0,\quad v=p^{2/3}>0,\quad
 \rho=v''>0 \quad(\ell<t<0).
\]
两端分别是原精确平端 germ 和简单 \(A_f\) 根 germ，并且
\[
 A_f=9v^2\rho,\qquad \rho(0)=0,\quad \rho'(0)<0.                \tag{1}
\]
原完整五门记为
\[
 F(U)=(\Delta_1,\Delta_2,\Delta_3,\Delta_4,\Delta_6).
\]
它们始终包含 R471 的端点多项式 \(P_H\)、真实八个单侧 primitive
系数，以及实际端点决定的 \(s,h,r_*\) 和归一。以下没有把这些端数据
作为不随一般 \(\rho\) 变动的外部常量。

先取一个真内部开窗 \(J\Subset(\ell,0)\)，与两个端 germ 有正距离。
在这个窗上 \(p,\rho\) 都有严格正下界。所有本节方向真紧支于 \(J\)。

## 2. 从紧支 profile 方向到真实 log 曲率方向

给定任意
\(\varphi\in C_c^\infty(J)\)，定义
\[
 \delta v_\varphi=\frac23p^{-1/3}\varphi',\qquad
 g_\varphi=\frac{(\delta v_\varphi)''}{\rho}.                   \tag{2}
\]
它们都是实际固定的 \(C^\infty_c(J)\) 函数；分母只在已选紧窗上使用，
没有在平端把 \(p\) 或 \(\rho\) 假定为统一正数。

考虑真实正曲率族
\[
 \rho_\epsilon=\rho\exp(\epsilon g_\varphi),                   \tag{3}
\]
并从原同一个左平端初值恢复
\[
 v_\epsilon''=\rho_\epsilon,\qquad
 p_\epsilon=v_\epsilon^{3/2},\qquad U_\epsilon'=p_\epsilon.
\]
因 \(g_\varphi\) 在左端附近为零，这仍是原真左 germ；因指数正，
所有有限参数都保 \(\rho_\epsilon>0\) 于内部。

在零参数求导。原恢复方程和原左初值给
\[
 (\dot v)''=\rho g_\varphi=(\delta v_\varphi)'',
 \qquad \dot v=\dot v'=0\text{ 于左 collar}.
\]
\(\delta v_\varphi\) 自己也在该 collar 为零，所以两个积分常数准确支付：
\[
 \dot v=\delta v_\varphi.
\]
继而
\[
 \dot p=\frac32\sqrt v\,\dot v
        =\frac32p^{1/3}\frac23p^{-1/3}\varphi'=\varphi',
 \qquad
 \boxed{\dot U=\varphi.}                                     \tag{4}
\]
最后一个积分常数同样由原左端支付。

因此 (2) 是一个完整的切向提升，不只是最高 jet 的替代：
\[
 D(\rho\mapsto F(U_\rho))[g_\varphi]=DF(U)[\varphi].            \tag{5}
\]
由于 \(\varphi\) 在右端整个邻域为零，(4) 同时给
\[
 \dot U(0)=\dot p(0)=\dot r(0)=0.                             \tag{6}
\]
所以这一特定方向的一阶端势、\(s,h,r_*\)、所有归一行系数确实不变。
这不适用于任意预选的 log \(\rho\) bump。

## 3. 五条适配列确实存在；十五条预选列没有免费收据

R481 对每个允许的精确平端 cap，给出五个分离支撑的真实
\(\varphi_i\)，使
\[
 \det\bigl(D\Delta_\nu[\varphi_i]\bigr)\ne0.                   \tag{7}
\]
按 (2) 逐个提升为 \(g_i\)，由 (5)
\[
 \det D(\rho\mapsto F(U_\rho))[g_1,\ldots,g_5]\ne0.            \tag{8}
\]
所以完整正曲率自由度确实覆盖 R481 的五个导数方向，并可由一次选定的
五条有限 log 曲率函数承载。

这与已经冻结的第一次 cap5 搜索有明确区别。该搜索使用五个细窗 bump
和十个宽窗 bump 的固定十五维空间
\[
 B_{\rm fixed}=\operatorname{span}\{B_1,\ldots,B_{15}\}.
\]
(8) 没有证明 \(g_i\in B_{\rm fixed}\)，也没有证明那十五列在任一参数点
都满秩。一般 \(g_i\) 含有 \(\varphi_i'\) 的两次导数及原 \(p,\rho\)
系数，既可变号，也不等于一个正 bump。指数参数化允许有号
\(g_i\)，因为保持正性的是 \(\exp(\sum\theta_i g_i)\)。

新运行给出的 Jacobian 若仅为浮点输出，只是该实际参数点的数值信息；
没有严格误差包含前，不把一个小 singular value 或一个浮点非零
determinant 称为原精确秩证书。反过来，该有限列的退化也不推翻 (8)。

## 4. 三条真 normal 可以准确恢复整个右 germ

(6) 是一阶结论。有限的 (3) 一般会在二阶及以上改变右端
\(U,v,v'\)，不能把它直接称为固定右 germ 的有限控制。

选一个与所有 \(g_i\) 支撑不交的真内部开窗 \(J_N\)。
在其中取三条待定紧支 log 曲率 normal \(n_1,n_2,n_3\)。
对任意原 log 曲率方向 \(n\)，记 \(d\rho=\rho n\)。直接从同一左锚积分：
\[
 d v'(0)=\int_\ell^0\rho(t)n(t)\,dt,
\]
\[
 d v(0)=\int_\ell^0(-t)\rho(t)n(t)\,dt,
\]
\[
 d U(0)=\int_\ell^0 K(t)\rho(t)n(t)\,dt,                       \tag{9}
\]
其中
\[
 K(t)=\int_t^0\frac32\sqrt{v(y)}(y-t)\,dy,\qquad
 K''(t)=\frac32\sqrt{v(t)}>0.                                 \tag{10}
\]
这里第三条保留了 \(U'=v^{3/2}\) 的真实累计；没有只恢复 \(v,v'\)
就假定 \(U\) 的常数自动正确。

在 \(J_N\) 选三个不同、有序的点。严格凸性 (10) 使
\[
 \begin{pmatrix}
 1&1&1\\
 -t_1&-t_2&-t_3\\
 K(t_1)&K(t_2)&K(t_3)
 \end{pmatrix}
\]
可逆。取三条足够窄但固定有限、积分非零的实际 bumps，
由连续性即使 (9) 的完整三乘三积分矩阵可逆。因 \(\rho>0\)，
其正权不改变这个结论。

现在使用同一个真实族
\[
 \rho_{\theta,\alpha}
 =\rho\exp\!\left(\sum_{i=1}^5\theta_i g_i+
                         \sum_{j=1}^3\alpha_jn_j\right).      \tag{11}
\]
有限维隐函数定理给唯一小光滑
\(\alpha=\alpha(\theta)\)，使
\[
 \bigl(U_{\theta,\alpha}(0),v_{\theta,\alpha}(0),
                         v'_{\theta,\alpha}(0)\bigr)
       =(U(0),v(0),v'(0)).                                   \tag{12}
\]
由 (6)，
\[
 \alpha(0)=0,\qquad D\alpha(0)=0.                             \tag{13}
\]
全部指数方向在两个端 collar 都为零，故 \(\rho\) 在那里准确不变。
左端使用同一原初值；右端由 (12) 和同一个 \(\rho\) 方程向后恢复，
得到整个右 \(v,p,U\) germ 准确不变。因此两个原端 germ、全部端 jets、
原简单根和根位置均保持，不只有限个端值。

内部 \(\rho_{\theta,\alpha}>0\)，所以 \(A_f>0\) 与无额外根也保持。
这一部分不需要把一个全平端上的 \(C^3\) 绝对小量冒作保号。

## 5. 完整八参数 block 和原端势

在 (11) 中考虑全部端数据和五门。其一阶 block 具有
\[
 D\bigl(v'(0),v(0),U(0),F\bigr)=
 \begin{pmatrix}
 0&B\\
 A&C
 \end{pmatrix},\qquad \det A\ne0,\quad\det B\ne0.              \tag{14}
\]
\(A\) 是 (7)，\(B\) 是 (9)。右下 \(C\) 是三个 normal 对完整五门的
真实影响；本稿没有把它置零，也没有丢掉其归一/端势贡献。
该 block 的可逆性不需要知道 \(C\) 的具体值。

在 (12) 的固定端流形上，(13) 使五门的一阶矩阵仍是 \(A\)。
有限映射随后使用完整原五门，因而仍可准确实现
\[
 F(U_{\theta(\epsilon),\alpha(\theta(\epsilon))})
        =(1-\epsilon)F(U)                                   \tag{15}
\]
于某个实际有限的 \(|\epsilon|<\epsilon_0\)。这是固定整个根 germ 的
真实五门径向下降，不是把有限 normal 费用归到零。

若用正状态计算，原端敏感度也可逐项写清。令
\(X=\log v,\ Y=\log v',\ Z=\log U\)，则
\[
 X'=e^{Y-X},\quad Y'=\rho e^{-Y},\quad Z'=e^{3X/2-Z}.
\]
对一个 log 曲率方向 \(b\)，
\[
 X_b'=X'(Y_b-X_b),\quad
 Y_b'=Y'(b-Y_b),\quad
 Z_b'=Z'(3X_b/2-Z_b).                                        \tag{16}
\]
原 \(p=v^{3/2},r=3\sqrt v\,v'/2\) 给
\[
 (\log r)_b=X_b/2+Y_b,\quad
 (\log s)_b=X_b-Y_b,
\]
\[
 H_b=H(Z_b-5X_b/2+Y_b),\qquad H=Ur/p^2.                       \tag{17}
\]
若 \(I_j\) 是未归一原积分，则
\[
 (A_j)_b=
 \frac{(I_j)_b-I_j\{5(\log r)_b+(8-j)(\log s)_b\}}
      {r^5s^{8-j}}.                                         \tag{18}
\]
一般方向要保 (16)—(18) 及端 \(P_H\)；只有 (2) 的特殊紧支提升才按
(6) 使这些端变化一阶为零。第一次 cap5 入口采用完整 (16)—(18)，
没有把其十五条原方向当作全部满足 (6)。

## 6. 一个有限模型的非零驻点意味着什么

取任意固定正定 \(G\)，目标
\[
 {\cal J}(U)=\tfrac12F(U)^TGF(U).
\]
若 \(F(U)\ne0\)，(7) 可选择一个真紧 \(\varphi\)，使
\[
 DF(U)[\varphi]=-F(U),
 \qquad D{\cal J}(U)[\varphi]=-F(U)^TGF(U)<0.                  \tag{19}
\]
按 (2)、(11)—(13)，这是一个保整个端 germ 的真实 log 曲率下降。

现在假设 \(U\) 恰位于某个预选有限参数模型的盒内点，并且该模型上的
**精确**一阶导数全部为零。则 (19) 的提升方向不可能落在该模型的
真实切空间中，否则模型一阶导数不可能全部为零。因此，非零的盒内
模型驻点确实存在模型外的允许下降方向。

这个结论的两个限制必须明说：

- 一个浮点 optimizer 的 optimality 数字不等于“精确驻点”；本稿
  不从数值输出反推一个未验证的等式。
- 若最优点在盒的边界，可能只需要放开盒内已有的一条方向；这时不能
  断言下降方向在原十五维线性 span 外。只能说有限盒不能证明整个允许
  cap 类无下降。

同样，六个有限起点都没有到零，只排这次实际运行所尝试的路径，
不是对全部允许 cap 的非存在定理。

## 7. 首次有限搜索之后真正新的任务

第一次 cap5 搜索没有自动消费 (2) 的适配方向。若它给出一个非零
最佳真实 cap，下一条不重复旧起点的明确入口是：

1. 直接消费该已付参数点及完整原积分，不重新恢复旧 self 或旧
   \(\psi_3\) 观察；
2. 在保留的真实平端内窗选 R481 的五个 \(\varphi_i\)，按 (2) 构造
   五条新 log 曲率函数；
3. 用一个不交窗口的三条 (9) normal 支付固定端约束；
4. 只对这个扩展后的新有限目标核其完整积分、正性和非退化量，再继续
   有限下降或针对一个候选作严格包含。

这是一个真正新增的有限控制问题。它不要求再跑原六起点或旧排名；
也没有因为存在新的局部下降，就保证经过有限次扩展一定到零。
统一步长、全局边界和零极限仍须由原五门与 R483 的真实紧化处理。

若选择一个新 cap 后需要全母库，仍须调用原从起点
\(q_4/F^\star/20\) 安装或已付小邻域内外分离接口。
这里的固定 cap 端 germ 不等于旧全母 \(F^\star\) 已固定，
更不等于实际 full \(J_{\rm aff}\)、全 period 或全部 \(s\) 段的同一
\(w_\theta\) 已支付。

## 窄核记录

尾成本代理只独立纸核了 (16)—(17) 的 log 状态链式；
原左锚提升 (2)—(5)、三 normal 的完整 \(U\) 累计 (9)、
固定端 block、模型驻点适用域由作者在本稿逐项给出。
没有把该窄核扩大成新搜索执行或零目标可达的收据。
