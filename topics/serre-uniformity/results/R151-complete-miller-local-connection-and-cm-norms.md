# R151. 完整真实 Miller 主函数、54个局部导数及CM/典范范数

日期：2026-11-12。**状态：已证明，完整304位/454步、全部54个局部导数及所有CM/典范范数均已完成。**证明与原始对象沿用 R117、R121、R140、R141、R145、R154、R159、R160；没有用主除子范数代替非主纤维的局部高度。

## 1. 固定实际对象和得到的函数

令
$$X=X_{\rm ns}^+(41),\quad g=54,\quad
D_0=K_f+D,\quad \mathcal L=\mathcal O(D_0),\quad\deg\mathcal L=126.$$
$D$ 为20个尖点，$K_f$ 为 R110 的固定典范除子，$f_0\in H^0(\mathcal L)$ 的零除子为 $D_0$。
R112 的真实 CM 类为
$$B=[A_B],\qquad A_B=Z_{-4}-D=E_B-D_0.$$
R121 已计算 $m=\#J(\mathbf F_{47})$，该整数304位，$m\bmod47=9$，并得到 $Y=mB\in47J(\mathbf Q_{47})$ 的完整真实点和对数。

本计算保留从 $B$ 到 $mB$ 的454次实际 AddFlip、每一步的325维主截面系数、真实负点二次截面及终点主函数。因此得到有限直线程序
$$\boxed{\operatorname{div}F=mA_B-A_1(Y),}$$
其中 $A_1(Y)$ 是 R141/R145 第一个54点 Abel 族的同一个度零除子。

计算环为
$$R_2=(\mathbf Z/47^4\mathbf Z)[i]/(i^2+1),\qquad q=47^4=4879681.$$
全部输入有已固定的实际模形式、挠点和积分提升来源。本文的函数系数在 $\mathbf Q_{47}$；不把随机下降得到的局部系数误称为全局有理系数。

## 2. 每一步确实是该主函数

对一实际点 $P$ 使用 $A_P=E_P-D_0$。
R117 的群运算返回 $R=-(P+Q)$ 和真正的三次截面 $s$，满足
$$\operatorname{div}(s/f_0^3)=A_P+A_Q+A_R.$$
完整199维乘积、252阶 colon 约束、126阶翻转约束及下降均在实际820个点上验证。清分母后的最大次数为630，小于820，因此不是孤立点拟合。

若已有
$$\operatorname{div}F_P=n_PA_B-A_P,\qquad
\operatorname{div}F_Q=n_QA_B-A_Q,$$
则
$$F_R=(F_PF_Qs/f_0^3)^{-1},\qquad n_R=-n_P-n_Q.$$
逐项计算其主除子给所需恒等式，说明逆号准确。
初始 $F_B=1$；若负点的二次截面是 $a$，则
$$F_{-B}=(a/f_0^2)^{-1}.$$

到最后的有效代表 $A_{\rm old}$，已有
$\operatorname{div}F_{\rm old}=mA_B-A_{\rm old}$。
完整理想的一维运输核给两个实际二次截面 $s_{\rm new},s_{\rm old}$，并以整个73维理想的单位同构验证其公共剩余除子相同。
若 $v_1$ 定义第一 Abel 族的完整126次基除子，则
$$g_{\rm tr}=
\frac{s_{\rm new}/f_0^2}{s_{\rm old}/f_0^2}\frac{f_0}{v_1},
\qquad
\operatorname{div}g_{\rm tr}=A_1(Y)-A_{\rm old}.$$
所以
$$\boxed{F=F_{\rm old}/g_{\rm tr}.}$$
这是函数和框架的实际变更，不只是两个 Jacobian 点的对数相等。

454步的所有真实点哈希与 R121 的独立已发布长乘逐项相同。
前67步的主截面曾从原前缀按同一随机状态补重放，全部系数哈希、点哈希及秩相等后并入；后面每一步直接保存完整系数。
两次内存137退出后均从295位原子检查点重做未保存的后缀，没有改变任何已保存步骤。最后使用仅改变保存频率及释放闲置JSON数据的 finisher，每完整位原子保存；数学、随机状态和逐步哈希校验全部保持不变。

## 3. 同一非形式第一变量的实际局部值

第二变量使用 R141/R145 的 $A_2(Q)$，特别取 $Q=Y$。
其126次代表中的固定72点在差中消去，故对实际函数 $\varphi$，
$$\varphi(A_2(Q))
=\prod_{j=1}^{54}\frac{\varphi(P_j(t_j(Q)))}{\varphi(P_j(0))}.$$
全部454步以及负点和终点运输在这些实际点的分母都为单位，所以四位精度完整保留。
Frobenius 下降使最后乘积属于 $\mathbf Q_{47}$。

按 R154 的规范，第一变量的 $[m]$ 群律给
$$m\,\lambda(e(A_B,A_2(Y)))
=\lambda(\sigma(A_1(Y),A_2(Y)))+
\log_{47}F(A_2(Y)).$$
R145 已计算同一个形式框架的值为4263370。
因此
$$\boxed{
\lambda(e(A_B,A_2(Y)))
=\frac{4263370+\log_{47}F(A_2(Y))}{m}\pmod q.
}$$
$m$ 在47处为单位，这一步没有精度损失。

实际得到
$$F(A_2(Y))=348741,\qquad \log_{47}F(A_2(Y))=3423668,$$
以及
$$\boxed{\lambda(e(A_B,A_2(Y)))=1730352\pmod{47^4}.}$$
完整454步文件为1340024字节，SHA256：
~~~
2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed
~~~
该值的对象是指定的 $\mathcal P_{B,Y}$ 范数元素；
它不是 $h(B,B)$，也不是 R148 规范 QC 截面的值。

## 4. 全54方向的真实局部导数

每个移动点使用实际整参数 $t_j$。对单位截面写
$$s_j(t)=s_{j,0}(1+r_1t+r_2t^2+r_3t^3+\cdots).$$
于是
$$
\log(s_j(t)/s_j(0))
=r_1t+(r_2-r_1^2/2)t^2+
(r_3-r_1r_2+r_1^3/3)t^3+O(t^4).
$$
从 $k\mathcal L$ 的截面扣除 $k$ 倍 $f_0$ 的展开，得到真正主函数的对数。
度零范数的对数是54项之和，所以其 $54\times3$ 系数矩阵没有被省略的跨点项。
按照第2节的同一符号递推，就得到 $\log F(A_2(Q))$ 的全部三阶系数。

每一步把54个参数代入 $Q=Y$，均与独立的54个实际值乘积的对数一致。
最终终点函数也作同一比较，不能把旧框架下的展开直接用于新框架。

令 $\Omega$ 为第二 Abel 族的真实切向矩阵，行参数满足
$$z_Q=t\,\Omega+O(t^2).$$
其中权二模形式必须乘 R123 的实际 Kodaira–Spencer 单位
$$\beta_0=-3/27652,$$
不是直接把权二函数当作 $dt$ 系数。
记 $\mathcal B$ 为 R141 已求出的 Hecke 修正矩阵，$z_Y=\log Y$。
第一侧实际反点函数为
$$\phi_Y=a_Y/v_1^2,\qquad
\operatorname{div}\phi_Y=A_1(Y)+A_1(-Y).$$
在 $Q=0$ 处，第二侧反点函数从二阶开始，所以 R140 的零双线性项框架给
$$
m\,\nabla_t\lambda(e(A_B,A_2(Q)))\big|_{0}
=
\nabla_t\log F(A_2(Q))\big|_0
+\frac12\nabla_t\log\phi_Y(A_2(Q))\big|_0
+\Omega\mathcal B^{\mathsf T}z_Y^{\mathsf T}.
$$
左乘 $\Omega^{-1}$ 并除以单位 $m$，得到54个 Lie 导数。

其严格精度为模 $47^3$。原因是 R140 的余项总次数至少四；
对第二变量求一次导数后，固定 $Y\in47J$，每项至少贡献三次47因子。
Hurwitz 系数的分母控制给
$n-1-v_{47}(n!)\ge3$（$n\ge4$），故所有高次余项都消失模 $47^3$。
程序保存全部54个系数，并核对真实全纯微分基的 Frobenius 下降关系。
它们是指定代数纤维的局部联络系数，不能自动替换全局双线性高度的54个系数。

## 5. 所有26个 CM 点及完整106次典范除子的范数

R160 已给26个实际点及0至16阶整盘展开，并证明它们及所有典范闭盘避开 $A_B$ 与新形式端点的支撑。
指定新的典范除子 $K_{g_1}$ 被准确分为4个一次因子与102次有限 étale 代数。
所用 $g_1/f_0$ 在全部26个 CM 点取单位。

在一个盘内，按 R159 写每个中间截面为
$$s=W_sU_s,\qquad W_s\ \text{首一 distinguished},\quad U_s\ \text{整单位}.$$
因为本条 $B$ 链的初始有效除子在所有这些盘都为空，准确递推为
$$F_n=V_n/W_n,\qquad
W_s=W_PW_QW_R,\qquad V_R=(V_PV_QU_s(0))^{-1}.$$
每步用实际首一多项式准确相除，并在最后从完整当前有效除子理想独立抽取因子作比较。
终点 $g_{\rm tr}$ 的共享零极也在函数层面相消。
所以这些计算没有通过数值上的47除法“恢复”已经丢失的精度。

实际出现的最高局部阶不超过4，0至16阶恰满足 R159 的一般精度界 $eN$。
在102次高因子上，每一步直接计算整数结果式范数并检查模47的互素性；全部真实中间范数为单位。
端点的高因子三个范数为
$$N(s_{\rm new}/f_0^2)=3358128,\quad
N(s_{\rm old}/f_0^2)=988985,\quad
N(v_1/f_0)=77312,$$
故
$$\boxed{N_{102}(g_{\rm tr})=1732217\pmod q.}$$
新、旧完整有效理想在该高因子上分别由实际有理截面见证互素，不只是比较点类。

完整实际数值为：

| 评价除子 | $F$ 的值或范数，模 $47^4$ |
|---|---:|
| $b=P_{-3}$ | 4861589 |
| $u=P_{-12}$ | 4060154 |
| $c=P_{-7}$ | 4390850 |
| $Q_2$ | 235692 |
| $T_2u$ | 2014683 |
| $T_2c$ | 3937027 |
| 典范低4次部分 | 3319877 |
| 典范高102次部分 | 1685667 |
| 完整 $K_{g_1}$ | 3504281 |

全26盘的非单位截面因子计数为 阶1：90次、阶2：38次、阶4：1次；低4典范盘为 阶1：37次、阶2：21次。这些是逐步局部因子次数的计数，没有用总赋值替代真实因子相消。
这里 $Q_2=2P_{-7}+Z_{-8}$ 的二重支点，以及 $T_2b=3P_{-12}$、$T_2P_{-7}=2P_{-7}+P_{-28}$ 的准确重数全部保留。

## 6. 已接到的真实 F2 第二变量

置 $F_2=27T_2+4$、$u=P_{-12}$、$c=P_{-7}$、$b=P_{-3}$。
R148 的真实第二变量除子，改用 $K_{g_1}$ 后分别为
$$D_u=27(T_2u+3u-Q_2)+4(u+b+K_{g_1}),$$
$$D_c=27(T_2c+3u-Q_2)+4(c+b+K_{g_1}).$$
前括号次数为 $-16$，后括号次数为108，总次数均为零。
由第5节的实际有限支撑范数直接计算
$$F(D_u)=
\left(\frac{F(T_2u)F(u)^3}{F(Q_2)}\right)^{27}
\bigl(F(u)F(b)F(K_{g_1})\bigr)^4,$$
以及把第一项 $T_2u$ 换成 $T_2c$、末括号 $u$ 换成 $c$ 的 $F(D_c)$。
实际得到：

| 第二变量 | $F(D)$ | $\log_{47}F(D)$ |
|---|---:|---:|
| $D_u$ | 4111193 | 3911622 |
| $D_c$ | 3862079 | 3354484 |

这些是 R154 后续搬运所需的真正主函数范数，没有将它们的对数单独称为全局高度。

改用 $g_1=h f_0$ 的准确值为
$$h(b)=344516,\quad h(u)=247689,\quad h(c)=3527523.$$
完成程序从实际73维系数重新取值核对这三个数。
R148 的规范截面坐标相应乘以 $(h(b)/h(P))^4$。
实际的新坐标及其对数为
$$\sigma_{F_2,b}(u):698837,\quad\log=152280,$$
$$\sigma_{F_2,b}(c):3999200,\quad\log=170469.$$
这些仍是规范截面在相应范数框架内的坐标及其对数，不包括框架本身的 Poincaré 高度。
因此典范除子更换所需的全局截面单位同样保留，没有另加一个未知拟合常数。

## 7. 已完成的两个CM混合形式输入

为继续两条真实 CM 链，R167 的实际 $m(P-b)$ 端点还给出同一 R141 框架的完整双逆计算。令第一变量在第一族，$mB$ 在第二族，程序重新构造第一变量负点及其真实反点主函数；第二反点函数复用 R145。
54个移动点的直接函数值乘积给两个真实度零范数，再按 R140 加入同一个 $\mathcal B$ 修正，得到
$$\boxed{\lambda(\sigma(m(P_{-12}-b),mB))=4548331,}$$
$$\boxed{\lambda(\sigma(m(P_{-7}-b),mB))=4557167\pmod q.}$$
完整的函数、范数、半对数和修正见 notes/2026-11-12-qc-cm-mixed-formal-and-local-unit-work.md 及其小证书。
这两项形式值已经完成；两条 CM 的304位非形式主函数链另继续运行，不能把备用终态入口当作已得到其全局高度。

## 8. 保存与复算范围

完整454步实际主函数数据保存在既有 p41_poincare_miller_jets47_saved.json.gz 路径；
它是后续在任意新支撑求范数所需的证明数据。
p41_miller_completion47_compact.json.gz 为8138字节，SHA256为69a33e8c944447e439804a842f418ea2f4e04b03ca5ccc8691a396e96036ffa0；它保存最终局部值、54导数、三阶展开、端点函数和各范数。
可重建的大型评价矩阵没有再次入库。

生成和评价入口：

- p41_poincare_miller_jets47.py，以及只改变内存释放/检查点频率的 p41_poincare_miller_finish47.py；
- p41_miller_cm_prepared47.py；
- p41_miller_canonical_low47.py；
- p41_miller_canonical_high47.py；
- p41_canonical_high_endpoint47.py；
- p41_miller_completion47.py。

全部最终数据均绑定同一完整链的 SHA，而不是混合不同滚动时刻。
本结果完成这条主函数和指定局部纤维的计算；R148 的全局规范截面及全部 CM 高度差仍按 open.md 的实际接口继续。


最终范数流水线 p41_finish_miller_pipeline47.py 串行运行全部评价；也可单独重算：
~~~
cp scripts/data/p41_poincare_miller_jets47_saved.json.gz /tmp/p41_poincare_miller_jets47_complete.json.gz
python -B scripts/p41_miller_cm_prepared47.py --script-dir scripts --miller /tmp/p41_poincare_miller_jets47_complete.json.gz --output /tmp/p41_miller_cm_prepared47_complete.json.gz
python -B scripts/p41_miller_canonical_low47.py --script-dir scripts --miller /tmp/p41_poincare_miller_jets47_complete.json.gz --output /tmp/p41_miller_canonical_low47_complete.json.gz
python -B scripts/p41_miller_canonical_high47.py --script-dir scripts --miller /tmp/p41_poincare_miller_jets47_complete.json.gz --output /tmp/p41_miller_canonical_high47_complete.json.gz
python -B scripts/p41_canonical_high_endpoint47.py --script-dir scripts --high-norms /tmp/p41_miller_canonical_high47_complete.json.gz --output /tmp/p41_canonical_high_endpoint47_complete.json.gz
python -B scripts/p41_miller_completion47.py --script-dir scripts --miller /tmp/p41_poincare_miller_jets47_complete.json.gz
~~~
其中 R145/R160 的可重建原始有限代数、54点三阶展开及现有 `/tmp` 输入按已发布恢复笔记准备；完整函数系数来自保存的454步文件，不重新执行群乘法。

汇总器初版将54维典范坐标直接与73维模形式值配对，Frobenius检查立即失败；已改成先通过 R110 的准确典范核嵌入 $K_1$ 转到73维，再重新取值。仅汇总步骤重跑，三个实际范数证书和完整链均未更改。
