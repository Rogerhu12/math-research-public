# 原 full47 的完整角作用：同一CM纤维与73维循环读取

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明有限读取方法；新角坐标尚待公开运行。**

## 1. 原对象和新目标

使用原 $Y=X_{\mathrm{ns}}^+(47)$、$q=4513$，
[R1090](../results/R1090-original-weight-one-integral-Hodge-source.md)
的95个真实Reynolds微分及73维Hodge整核。
[R1096](../results/R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
给原行作用矩阵 $H=T_3+T_5$，其特征多项式 $P$ 的degree73、
模$q$判别式2650；$\mathcal T/q=\mathbf F_q[H]\simeq\mathbf F_q[X]/P$。

新目标是
[R1078](../results/R1078-original-level47-Cartan-correspondences-and-fixed-cycles.md)
的全部23个真实非恒等角对应 $R_C$，
$C=0,2,\ldots,23$，在**这个原Hodge格**上的实际多项式
$$
R_C=p_C(H),\qquad \deg p_C<73.
\tag{AH.1}
$$
不从抽象角域或一维Hecke标签猜测 $p_C$。

输入点固定为R1105的候选76，$j=-3375$。
其已认证的同一模型为
$$
E/\mathbf F_q:\ y^2=x^3+786x+524,\qquad
j(E)=1138,\qquad a_q=0 .
$$
完整47挠域次数为4。原tag在25条Frobenius固定项链中唯一选出此点；
旧消费者已固定 $I^2=-1$ 标记及实际Weil根2。
本次只重建该已完成输入，逐字核其coarse95切向SHA，
不重开旧235盘、5453点筛选或八点切向任务。

## 2. 完整几何纤维的determinant-one表示

固定该原 $E$ 与其Weil基 $(P,IP)$，
令 $I=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$。
每个无定向necklace唯一表示为
$$
I'=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad
a^2+bc=-1,\qquad I'\sim-I'.
\tag{AH.2}
$$
因为$-1$在$\mathbf F_{47}$非平方，$b\ne0$。
枚举$a$和$b\ne0$，令$c=(-1-a^2)/b$，再除$\pm$，
准确得到 $47\cdot46/2=1081$ 个原目标，没有新增或遗漏scalar分支。

角由原式
$$
C=[-\operatorname{tr}(II')/2]=[(c-b)/2]\in\mathbf F_{47}/\pm
$$
取得。恒等角1恰一个目标，角0有24个，其余22角各48个。

对每个$I'$选择向量$v=(u,v_2)^t$满足
$$
\det(v,I'v)=cu^2-2auv_2-bv_2^2=1.
\tag{AH.3}
$$
左边是非退化各向异性二元型，非零值由有限二次域的norm满射取得，
故一定存在。实际程序只枚举$\mathbf F_{47}^2$并逐项验证(3)。
于是
$$
g=(v,I'v)\in\operatorname{SL}_2(\mathbf F_{47}),\qquad I'g=gI.
$$
所以 $(P',Q')=(P,IP)g$ 既标定$I'$，
又**保留原实际Weil根2**。不同满足(3)的选择相差原determinant-one
Cartan；$I'\mapsto-I'$相差原normalizer。完整两phase Reynolds源
已证明对这些变化不变，故没有重新选择一个未配准的cyclotomic根。

## 3. 全部目标共用原2208挠点数据

只计算一次原全部2208个非零挠点与weight-one值$e_x$，
使用R1105的真实加法链、奇性及Frobenius检查。
目标$g$的值仅将标签重排为$e_{gx}$。
每个原描述子$(a,c,d)$仍按
$$
G_{a,\rho}(g)=
 \sum_{x\ne0}\left(2^{aN(x)}e_{gx}e_{g\rho x}
                 +2^{-aN(x)}e_{gx}e_{g\bar\rho x}\right),
\qquad \rho=d+ci ,
\tag{AH.4}
$$
逐项读取。每个范数类的24半向量乘二，
两个phase、实/虚约定和全部95描述子均保持原定义。

**单个目标未必在$\mathbf F_q$上，不能逐目标强制降域。**
所有中间值保留在同一个已标定 $\mathbf F_{q^4}$。
同一角的全部目标完成求和后，对每个结果检查
$a^q=a$以及非恒定坐标全部为零，再把常数整数传给Sage。
这是定义于$\mathbf Q$的原对应作用的实际下降；
每个几何目标按同一纤维重数1进入。

基点$j=1138$不等于0、1728；
该纤维所有目标都是同一非特殊$j$的不同项链，源/目标$j$参数均étale。
角对应保持同一$E$及$\omega_E=dx/(2y)$，
故源与所有目标的KS frame相同。由原式
$$
dj=\frac{124416A^2B}{4A^3+27B^2}\mathrm{KS}
$$
把整个角和乘同一非零因子，即得实际 $dz$ 系数，
$z=j-j(y)$。不产生未付的稳定子或isogeny尺度。

## 4. 一个循环评价为何唯一确定完整73维算子

记原Hodge基为列$\omega=(\omega_1,\ldots,\omega_{73})^t$，
已认证矩阵约定为 $H^*\omega=H\omega$。
设
$$
e=(\omega_i/dz)(y),\qquad
u_C=((R_C^*\omega_i)/dz)(y).
$$
由§3，$u_C$就是角目标的真实95值先求和再乘原73维核的列。

原角对应与全部away-47 Hecke对应交换：
prime-to47 isogeny输送完整47挠点标记并保角；
两种有限模问题的fiber product给真正对应交换。
R1087已经将此作用接入原Jacobian，不是仅置换表示的作用。
另一方面$H$在完整73维Hodge上的特征多项式平方自由且degree73，
故其中央化子恰为$\mathbf F_q[H]$。所以真实$R_C^*$一定且唯一有(AH.1)。

本次实际先检查
$$
C_e=[e,\ He,\ldots,H^{72}e]
\tag{AH.5}
$$
行列式是否非零。若非零，
$$
C_e\,\operatorname{coeff}(p_C)=u_C
\tag{AH.6}
$$
唯一给完整73维真实角算子。这里不需要先知道角的抽象谱与Hecke谱如何配对。

若(AH.5)不满秩，程序以真实未完成结论退出；
不将十六个一次坐标的旧非零冒充全部28块非零。
这是新有限证书需要读取的数值。
后继可以换一个具体原点或使用多点评价，不把失败当数学零结论。

## 5. 完整结构核对与实际两个稀疏方向

新坐标取得后，消费者核：

1. 恒等角的值给常数多项式1，且
   $1+\sum_{C\ne1}p_C=0\bmod P$，即原 $j^*j_*=0$。
2. 23个非恒等角的多项式系数矩阵rank23。
3. 每个$p_C(H)$的迹等于R1078原fixed-cycle迹$\tau_C$，
   包含原CM2/3稳定子及全部23cusps。
4. **全部** $23^2$ 对的原完整composition
   $$
   p_Ap_B=d_A\mathbf1_{A=B}
          +\sum_Dn_{A,B}^{D}p_D\pmod P .
   \tag{AH.7}
   $$
   这里$n_{A,B}^{D}$逐项使用R1078已证明、R1081已认证的闭式。
   本次是新坐标桥的完整核对，不重新宣称旧fiber-composition证明。

另读取
$$
Z_A=13R_0+4R_2,\qquad Z_B=2R_4-7R_0 .
$$
核两者实际trace0及
$\operatorname{Tr}(Z_A^2)=336288\bmod4513$，
并给$\gcd(P,p_{Z_A},p_{Z_B})$的degree。
共同零块或退化结果都合法，不因目标需要而强制改为非零。
这些算子及$\mathcal F_3^*,\mathcal F_4^*$的后续作用
均可由全部$p_C$直接组成。

## 6. 执行和输入边界

脚本 [full_p47_original_angle_Hodge_action.py](../scripts/full_p47_original_angle_Hodge_action.py)
只在本公开仓库Actions运行，固定官方SageMath10.6 image与
python-flint0.9.0。数学1200秒，预留30秒。
Sage父进程只消费原Hodge/Hecke格与进行$\mathbf F_q$线性代数；
fresh-exec纯Python子进程只做原域运算。
原生库、所有源SHA、真实checkout和两README均在请求中固定。

父进程先从原基点评价核(AH.5)，再向子进程发继续消息。
两个进程共用同一绝对截止；没有为子进程另给1200秒。
单角完成即打印其完整95和的hash与目标表示hash；
原95向量只经过runner进程管道，不上传artifact或Release。
最终回执须同时含全部24个含identity纤维、1081目标和所有(AH.7)核对。

可复用API：
`field_targets()` 给原有限纤维与det1标记；
`OriginalReynoldsValues(field,descriptors,grid).values(g)`
给保扩域的原95值；
`recover_angles(source,H,probe,field_rows,req)`
给真实$p_C$、循环矩阵及完整证书。
后继同一runner内可直接使用这些对象；可重算数组不入库。

成功只支付原角作用的实际Hecke坐标。
R1103的局部$\alpha$、原CM类坐标及最后QC共同根排除仍须实际完成，
固定47更不替代全$p$的Serre完成标准。
