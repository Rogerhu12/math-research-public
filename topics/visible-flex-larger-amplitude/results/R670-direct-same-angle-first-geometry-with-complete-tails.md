# R670. 完整同角低模包围与新父自身的连续首 jet 几何

日期：2026-11-20。会话：Astra-resume-public-20261120 / recover_evidence。

**状态：已证明的连续区间算法与公开 Actions 实现；本条发表时没有执行新候选的科学计算。** 本条不继承旧候选的 SHA、逐胞支持下界或局部证书。具体新父是否通过，须以本仓库 Actions 对该次实际数组返回的报告为准。R663、R665、R667 的已登记数值不在这里重算或改写。

## 1. 对象与结论

沿用 [R656 的准确闭场](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)、R662 的同载体准确重建以及 [R667](R667-same-angle-C1-transfer-and-complete-closed-embedding.md) 的完整余项规则。数学对象在此重新列明。

每个原节点为 $s_i=\alpha_iS+\gamma_i$，$\alpha_i,\gamma_i$ 是准确有理数，$S,R$ 由同一 FullHold 积分定义及其有理外盒确定。全部自由系数按保存的 binary 数作为准确实数解释；派生 core 切向系数按准确实乘法 $T_j=-2jc_j$ 重建，不能把它另存的舍入槽当作第二组自由变量。原共享三 jet 定义每胞唯一五次 $q$；原仿射端口保持。

令 $\nu_j=2j$，并置

$$
\rho=1+\sum_{j=1}^M(1-\nu_j^2)c_j\cos(\nu_j\phi),
\qquad
\delta=\sum_{j=1}^M\frac{1-\nu_j^2}{\nu_j}c_j\sin(\nu_j\phi).
$$

$\Theta=\phi+\delta$，$e_r(\delta)=(\cos\delta,\sin\delta,0)$ 为旋转 $\phi$ 架中的完整解析向量。实际场是

$$
X=q+\chi H e_z+f e_r(\delta),\qquad f=\chi(R+S-s).
$$

$\chi$ 为原宽度的五次 smoothstep。记真实欧氏切向量 $V=X_s$、$T=X_\phi$，其中 $T$ 包含旋转架的连接项。取

$$
N=T\times V,\quad E=|V|^2,\quad W^2=|N|^2,\quad
A_\beta=\operatorname{diag}(1,1,\beta),\quad0<\beta\le1.
$$

本条给出一个不借旧逐胞证书的完整算法：对全部原胞、全部角、上下镜像及两圆盘，返回 $E,W^2$ 下界，支持量

$$
\sigma_\beta=\frac{(A_\beta X)\cdot N}{|N|}
$$

的下界，以及位置范数上界、固定见证点距离下界。若全域 $W^2>0,\rho>0,\sigma_\beta>0$，则原闭 $C^2$ 参数球是嵌入。所有下界及上界均针对完整场；“低模”仅指哪些有限多项式使用角区间变换，未保留部分全部另付绝对余项。

默认低模数为24、解析指数 Taylor 次数为8；这两个数均是算法参数，不是删去方程或改变候选的模型参数。

## 2. 径向准确重建

对胞宽 $h=s_{i+1}-s_i>0$，五次 Hermite 的 Bernstein 控制点为

$$
Y_0,\quad Y_0+\frac h5U_0,\quad
Y_0+\frac{2h}5U_0+\frac{h^2}{20}A_0,
$$

$$
Y_1-\frac{2h}5U_1+\frac{h^2}{20}A_1,\quad
Y_1-\frac h5U_1,\quad Y_1.
$$

逐项区间代入准确 $h$ 外盒和准确 binary jet 即包围真实控制点。导数用

$$
b'_j=\frac d h(b_{j+1}-b_j)
$$

得到，$d$ 为当前 Bernstein 次数。在原 $\chi$ 断点处分 piece；该分割使用准确 $S-\mathrm{width}$，不使用浮点网格间隙判断替代。$\chi$ 次数5，$f$ 次数6，因此 $X,T$ 的径向系数次数不超过6，$V$ 不超过5。全部升阶至6，再用准确有理二分参数进行 de Casteljau 细分。

其中高度必须先在同一控制点组合 $q_{Z0}+\chi H$，速度先组合 $q'_{Z0}+\chi'H$。先分别取绝对值会破坏真实的大数抵消，本算法没有这样做。

对固定角的每一分量，Bernstein 基非负且和为1。因此只要每个控制点的完整角值在一个区间内，整个径向子胞都在这些区间的凸包内。径向细分后重复同一论证即可；没有把节点或 Gauss 样值当成连续界。

## 3. 完整解析 lift 的有限 Laurent 部分与余项

写 $d_j=(1-\nu_j^2)c_j/\nu_j$，$z=e^{2i\phi}$。则

$$
i\delta=\sum_{j=1}^M\frac{d_j}{2}(z^j-z^{-j}).
$$

该 Laurent 多项式的系数是实数。对整数 $K\ge1$，准确展开

$$
P_K=\sum_{k=0}^K\frac{(i\delta)^k}{k!}.
$$

每次卷积保留全部支撑，不截去中间高频。因 $\delta$ 是实数，指数函数沿实相位的积分余项满足

$$
|e^{i\delta}-P_K|
\le\frac{|\delta|^{K+1}}{(K+1)!}
\le \tau_K:=\frac{(\sum_j|d_j|)^{K+1}}{(K+1)!}.
$$

这是实相位余项；不需要额外的 $e^{|\delta|}$ 因子，也不把它误用成复相位界。

若 $P_K=\sum b_jz^j$，其 cosine、sine 系数分别为 $b_j+b_{-j}$ 与 $b_j-b_{-j}$。先把前 $M$ 模与原 $q$ 的相同控制系数组合。超出 $M$ 的全部 Laurent 系数用 $l^1$ 范数付清；cos、sin 两个尾的欧氏范数给完整水平向量余项。再加 $\tau_K$，得到 $\varepsilon_r$。

角切向量的解析部分为 $f\rho e_\theta(\delta)$。源码先准确展开完整的 $\rho P_K$，包含其全部至 $(K+1)M$ 的 Laurent 支撑，再做同样的有限部分与尾分离。指数余项乘以已经向外包围的 $\|\rho\|_\infty$，得 $\varepsilon_{\rho r}$。故

$$
X=X_{\rm fin}+R_X,\qquad
V=V_{\rm fin}+R_V,\qquad
T=T_{\rm fin}+R_T,
$$

$$
|R_X|\le \|f\|_\infty\varepsilon_r,\quad
|R_V|\le \|f'\|_\infty\varepsilon_r,\quad
|R_T|\le \|f\|_\infty\varepsilon_{\rho r}.
$$

余项只有水平分量；源码对两个水平分量各加入该向量上界，对高度不虚加解析余项。该做法略保守而严格。这里的 $X_{\rm fin},V_{\rm fin},T_{\rm fin}$ 已包含原全部 $M$ 模与有限解析项之间的抵消。

## 4. 低模同角闭弧包围

对上述有限部分，再选 $1\le L\le M$。前 $L$ 模作区间三角变换；第 $L+1$ 至 $M$ 模在每个径向 Bernstein 控制点按系数绝对值和加入余项。其后再加第3节的完整解析余项。两种尾都保留，不能因为实际高模很小就删去。

令 $Q>4L$ 为二幂，均匀中心为 $\phi_k=2\pi k/Q$，闭弧半宽 $\Delta=\pi/Q$。有限多项式的实际最高频率是 $d=2L$。设

$$
\eta=1-\frac{d^2\Delta^2}{2}>0.
$$

对任意一个准确的有限三角多项式 $p$，有

$$
\|p''\|_\infty
\le \frac{\max_k|p''(\phi_k)|}{\eta}.
$$

证明：在 $|p''|$ 取最大值处，若最大值不为0，其相应带符号分支的一阶导数为0。取最近的网格中心，用二阶 Taylor 余项及三角 Bernstein 不等式
$\|p^{(4)}\|_\infty\le d^2\|p''\|_\infty$，移项即得。最大值为0时结论直接成立。

因此同一闭弧上

$$
|p(\phi)-p(\phi_k)|
\le \Delta|p'(\phi_k)|
+\frac{\Delta^2}{2\eta}\max_\ell|p''(\phi_\ell)|.
$$

源码使用 f512 的向外整数 twiddle/radix-two interval transform 支付三个网格量，并把此 Taylor 损失及全部尾相加。上述证明逐个适用于控制点区间中每一个真实系数选择，因而区间最大上界仍统一有效。

$X,V$ 在旋转架中的分量奇偶为 $(\mathrm{cos},\mathrm{sin},\mathrm{cos})$，$T$ 为 $(\mathrm{sin},\mathrm{cos},\mathrm{sin})$。范数、支持量和 $W^2$ 因而具有半周周期与反射对称性，只需覆盖 $0\le\phi\le\pi/2$ 的闭弧。保留端点弧，弧之间允许重叠。此处仅减少完全重复的覆盖，不改变场或遗漏独立角区域。

## 5. 在同一盒内计算有符号支持量

对同一径向子胞和同一角闭弧，将第2–4节得到的三向量分量区间记为 $\mathcal X,\mathcal V,\mathcal T$。逐分量区间乘加得到

$$
\mathcal N=\mathcal T\times\mathcal V,\qquad
\mathcal E=|\mathcal V|^2.
$$

面积平方的两种恒等式均严格包围同一准确量：

$$
\mathcal W_a^2=|\mathcal N|^2,\qquad
\mathcal W_b^2=|\mathcal V|^2|\mathcal T|^2-(\mathcal V\cdot\mathcal T)^2.
$$

取两下端点之最大、两上端点之最小仍是合法外盒。若其下端点和 $\mathcal E$ 下端点严格为正，可取向外平方根和区间除法：

$$
\mathcal S=
\frac{(A_\beta\mathcal X)\cdot\mathcal N}{\sqrt{\mathcal W^2}}.
$$

分子在同一盒内保留符号。未把 $\mathcal X$、$\mathcal V$、$\mathcal T$ 改成来自不同角的独立全周极值，也未先用旧父法向锥传递。分量乘法仍可能保守，但所得下界无条件正确；若未正，只记未付，不解释为真实负支持或非嵌入。

对子胞和角弧取最小，即得原胞下界。不同加密层对同一原胞给出的下界可取最大，上界可取最小，因为它们都对同一个完整胞有效。这样只需加密尚未达到指定支持预算的胞，无需重复已经充分的胞。

## 6. 两盘、镜像与完整嵌入

原仿射端口使 core 镜像二阶相容，也使末圈准确满足

$$
X=R e_r(\Theta)+He_z,\quad X_s=-e_r(\Theta),\quad X_{ss}=0.
$$

所以补上两平圆盘后仍是原闭 $C^2$ 参数球。上盘支持量为 $\beta H$，下盘镜像相同；盘心用 Cartesian 图处理，不把极坐标的参数退化当作浸入失败。活动上下片的范数、面积和带 outward 取向的支持量由镜像保持。

若全部胞 $W^2>0$、$\rho>0$，且全闭面支持量至少 $\sigma>0$，则 $X\ne0$，并且向量场 $A_\beta x$ 不切于该面。对线性流

$$
x\longmapsto e^{tA_\beta}x
$$

沿轨道投影到单位球。因 $\beta>0$，每条非零轨道与单位球恰交一次，投影光滑，微分核恰为 $A_\beta x$ 的直线。故投影与闭参数球映射的复合是局部微分同胚。紧性使其像既开又闭，且它是单位球的覆盖。单位球单连通，连通覆盖只能一层。因此该复合为微分同胚，原 $X$ 必单射；紧浸入于是是嵌入。这也给出 R650 正定流论证在本接口中的完整应用。

活动相位的固定材料换元要求 $\rho>0$；水平旋转与 $A_\beta$ 对易。因此原族的各相位使用同一支持与浸入界。此论证不要求当前 Gram 误差已经小到 $10^{-6}$，但它也不证明等距方程已求解。

## 7. 同次位置盒支付直径与 held 见证

令

$$
P=1+\sum_{j=1}^M c_j,\qquad p=(0,P,0)=\operatorname{Rot}_{\pi/2}X(0,0).
$$

源码按准确 Fraction 求 $P$。在旋转 $\phi$ 架中，

$$
p_\phi=(P\sin\phi,P\cos\phi,0).
$$

$\sin\phi,\cos\phi$ 用同一严格角中心 twiddle，并以一阶项及二阶导绝对值上界1支付闭弧余项，绝不使用普通 libm 数值当作外盒。对每个已有 $\mathcal X$ 同时计算

$$
|\mathcal X|^2,\qquad |\mathcal X-p_\phi|^2,\qquad
|\mathcal X+p_\phi|^2.
$$

**固定 $p$ 不具有支持量的全部反射对称性。** 本算法保留两种符号：$x$ 轴坐标反射固定 $p$，$y$ 坐标反射交换 $p$ 与 $-p$；半周旋转也交换两者。上下 $z$ 镜像固定 $p$。因此四分之一角区间上的两符号下界覆盖完整上下活动面。只计算 $+p$ 将不正确。

平圆盘的位置范数平方不超过 $R^2+H^2$，到 $p$ 的距离平方准确为

$$
H^2+\max(0,|P|-R)^2.
$$

若完整覆盖得到 $B\ge\sup|X|^2$ 与 $d^2\le\inf|X-p|^2$，则

$$
D\le 2\sqrt B,\qquad \operatorname{dist}(p,\mathcal S_0)\ge\sqrt{\max(0,d^2)}.
$$

$p$ 属于 $\pi/2$ 活动相位的 core；固定帽提供 held 识别。因此在已经证明闭嵌入的前提下，R248/R650 的同一比较给 held 幅度下界。不需旧6077或旧0241的直径、held 下界。返回的数可能较松，但已覆盖全像。

在 $\beta=1/4,H>1,R>9/20$ 时，还可直接用 R661/R663 的四个固定 $p_4$ 帽 marker：高度 $h=1/1000$，支撑半径互异，marker 支持至少 $64/267$。其条件直径上界增加 $2h$，见证距离取原下界与 $H-h$ 的较小值，固定 grip 直径为 $9/10$。这几个数均向外运算。

只有对这个新父另付 R661 的全部原胞非平面条件，并实际得到正 held 见证后，才标记四个 marker 支付正 Euclidean 形状距离。源码调用已刊准确系数读取器一次；不把旧父非平面结论复制给新父。没有付数值的 $\delta_E$ 下界，也没有付全域曲率或 reach。

## 8. 实现、公开执行参数与可信度

完整入口为 [actions_closed_postprocess.py](../scripts/resume_20261120/actions_closed_postprocess.py)，本条版本：

- 59417 bytes。
- SHA-256：eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599。
- direct 命令调用的已刊径向/lift 源分别绑定 R656、R662、R665 和 f512 的源 SHA；这些源不改字节。
- 新源在本地仅经 AST 语法解析；未导入执行科学代码，未运行小模型、旧父或 a04。
- 程序仅在本公开仓库 GitHub Actions 环境中允许进入科学计算。每份输出记录实际 run、commit、候选、node report 和依赖 SHA。

默认公开命令如下，WORK 指当前 Actions 重建目录：

    python topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_postprocess.py direct \
      --repo "$GITHUB_WORKSPACE" --work "$WORK" \
      --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-next-six.npz" \
      --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
      --plan 256:1,512:2,1024:4,2048:8 \
      --low-modes 24 --taylor-degree 8 --beta 1/4 --target-support .14 \
      --cells all --out "$WORK/postprocess/direct-a04-first-geometry.json"

首层覆盖全部922胞；后层只读取本次报告中尚未达到 $.14$ 支持预算或浸入未付的胞。$.14$ 是后续 reach 估计的预算目标，**不是闭嵌入的新定义**：全域严格正支持即支付嵌入；若正但低于 $.14$，程序分别记录二者。若仍有未付胞，报告保留其准确 scope，不把任务或报告截尾当作成功。

入口允许明确指定本轮 continue 的实际 bundle，并接受自定义 carrier 与可重复的 manifest。direct 的连续覆盖本身不依赖有限见证位置；它记录这些位置的来源、当前 carrier 身份及是否属于当前 bundle，丢弃历史几何值，不另重算一份有限点几何。完整覆盖成立时这些域内位置自然已在覆盖中。tail 子命令则逐个实际重读 manifest 位置，二者在输出中分别标明。

位置、支持、面积、见证界的 arithmetic 是向外 IEEE binary64：准确 Fraction 输入、四则与平方根后 nextafter、f512 严格三角变换、完整尾项。假设标准 IEEE 运算及非 FTZ 与 R656 相同。源码不把普通 float 六 jet 曲率读取混入此证书；tail 子命令是 R669 的另一个数值诊断，可信度单独声明。

**本条没有新的候选应用数值。** 将来应用记录必须列实际 Actions run、实际数组与输出 SHA；旧 a04 名称只是重建链位置，不能预先当作历史 a04f9f 的准确系数。


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
