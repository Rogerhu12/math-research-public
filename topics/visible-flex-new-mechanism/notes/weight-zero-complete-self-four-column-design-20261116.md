# 权零完整 self/current 的四列最小新观察设计

日期：2026-11-16。本文是新运行合同与纸面来源说明，**尚未执行**。原 Q 秩、current 秩、原 53 self 秩、原 pure 成员、旧人工检查、旧 forcing 和 profile 评价全部复用；不运行这些旧目标。新运行只消费下列四条准确成本的完整 self 累计量及其唯一权零 current 校正量。

## 1. 新问题、已付空间及真实边界

记 $E=(\pi,\mathcal Q)$，$\mathscr C$ 为 R433/R434 的完整三矩有序 current，$\mathcal K_0=\mathcal R_0\cap\ker(E,\mathscr C)$。R462 的纸面维数接口为
$$
\dim\mathcal K_0=5.
$$
既有 49 模块的真权零完整成本仅给三个独立类
$$
\mathcal K_8,\quad V_{51},\quad V_{52}.
$$
这里 $\mathcal K_8=\delta^8\mathcal K_0^{\rm loc}$ 是 R435 的局部串，**不是** R316 按原 nonpivot 编号的 $K_8$。下文用 $K_8^{\rm old},K_9^{\rm old}$ 区分后者。

R465 的完整零权增强商接口需要两个正常目标的同一镜对 self 是否同时落入 $S(\mathcal K_0)$。R451/R459 的最高项及固定宽度右逆不提供这两个完整值；只算两个响应补列不能宣称这两个成员门已付。因此根明确把本次唯一新观察限定为四列：

1. $K_8^{\rm old}$ 经已付 whole-Q 右逆、再经唯一 current 右逆校正；
2. $K_9^{\rm old}$ 作同样校正；
3. $X_H=H_*+J_4$ 经唯一 current 校正；
4. $X_Y=J_4-J_6$ 经唯一 current 校正。

原型、桥、正成本与实际截面的基准不因线性观察而消失。本次仅给完整函数和精确差证书，不把 signed 成本当真实路径，不宣实际全 period 或同一 gauge 已付。固定物理镜对与全仿射闭包的成员问题也不以任意 profile 采样替代。

## 2. 全部成本采用 R126 原 old 列号

$E_8$ 用 $P,R,S,L,U,V,T,Y$；其中 $V=\Phi_{p_1}$，$Y=\Phi_{p_2}$。R126 原 old 列与完整三槽定义保持：
$$
C(A,B)(a;b,c)=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)).
$$

四目标展开给出的准确必需原响应集合为
$$
\boxed{\{0,2,3,4,5,7,8,9\}.}
\tag{1}
$$
八个而非九个原响应的原语依次为
$$
B_LC(V,Y),\ B_VC(L,Y),\ B_VC(V,T),\ B_VC(Y,U),\
B_V\tau_{109},\ B_YC(L,T),\ B_YC(V,U),\ B_YC(Y,R).
$$
$\tau_{109}$ 是原 W35，不可擅换为 $\chi_{109}$。

两个 pure 核是已付完整原式：
$$
K_8^{\rm old}=R_8-2R_0+5R_2-R_3,\qquad
K_9^{\rm old}=R_9+6R_2-\frac83R_3.
\tag{2}
$$
两正常目标为
$$
\begin{aligned}
X_H={}&C_2+C_4+\frac{31}{32}R_2-\frac3{128}R_3
+\frac{31}{64}R_4-\frac{39}{32}R_5+\frac{27}{128}R_9,\\
X_Y={}&C_4-C_6+\frac{35}{256}R_2-\frac3{1024}R_3
+\frac{35}{512}R_4-\frac{39}{256}R_5
-\frac1{64}R_7+\frac{27}{1024}R_9 .
\end{aligned}
\tag{3}
$$
(3) 已由 R316/R333 同一完整 $E$ 成员关系付 $\pi=\mathcal Q=0$；本次不再测其 pure 或 Q。

三 normal 原根的状态键按 $(h,k,\omega,\log h)$ 排列：
$$
C_2:(0,2,0,0),\quad C_4:(0,4,0,0),\quad C_6:(1,1,1,0).
$$
原 mixed $-2$ SHA256 分别为：

| 根 | SHA256 |
|---|---|
| $C_2$ | b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f |
| $C_4$ | 1d67672bb734f602675f84768b8afd62363d3742ca203ea01b23c9b1f3f0b592 |
| $C_6$ | 5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02 |

原 reference/Gamma SHA 为
c6276335dd47380509870798123478dc1b5a25ad83f3eef15d30cedcef4ece0b。
所有 $N_0$、同一 Gamma、参考态及原 history 留在原根内。本次只读取、解码和恢复上述必要原 mixed 输入；不重新编译 forcing，不读纯根反造 mixed。

## 3. 两个补列为何确实是剩余完整成本方向

这一节是原 sl2、Jacobi 和既有维数的纸面有限推导，不是新 rank 运行。

R316 的十三 pure 核按 old nonpivot 编号为
$1,4,5,7,8,9,10,11,12,13,15,17,19$。
真权零 $B(E,Z)$ 的十列在这些核中的准确表达为
$$
\begin{array}{c|l}
-B_LH_6/8640&K_1\\
 B_UH_6/2880&4K_8-4K_4-3K_{15}\\
 B_VH_5/1920&K_4\\
 B_TH_5/1920&K_{15}-K_{11}-K_7+K_1+2K_{17}\\
 B_YH_4/96&-5K_7-12K_8-K_9-5K_{10}+K_{11}\\
 B_YJ_2/4&8K_8-6K_9+K_{11}\\
 B_V\chi_{109}&K_5\\
 B_T\chi_{109}&K_{19}+K_{17}/4\\
 B_Y\chi_{40}&K_{12}+K_8/32\\
 B_Y\chi_{104}&K_{13}-K_7/16-3K_8/8+3K_9/16 .
\end{array}
\tag{4}
$$
这些十列由三角消元独立。其商可取 $[K_7],[K_8],[K_9]$。

原 $\delta$ 的完整 Leibniz 公式又给
$$
[\mathcal K_8]=322560(3[K_7]+20[K_8]-12[K_9])
\tag{5}
$$
模上述十列。因此 $(\mathcal K_8,K_8^{\rm old},K_9^{\rm old})$ 给三维商的一组完整成本基。式(5)并非只在 Af 点作微分；先在完整原算子上做 $\delta^8$，最后才取商。

可手核(5)的最短有限表：设
$$
\begin{aligned}
v_0&=P,\quad v_1=-2(R+S),\quad v_2=8(U-L),\\
v_3&=12(4V-T),\quad v_4=-96Y,\\
w_0&=R-S,\quad w_1=4L,\quad w_2=-2(4V+T).
\end{aligned}
$$
模 $B(E,Z_{71})$，$\mathcal K_0^{\rm loc}=-B_PC(P,R-S)/2$。
$\delta^8B_PC(P,R-S)$ 的六项 multinomial 系数依次为
$70,280,280,420,560,420$，槽为
$(v_4,v_4,w_0),(v_3,v_4,w_1),(v_4,v_3,w_1),
(v_2,v_4,w_2),(v_3,v_3,w_2),(v_4,v_2,w_2)$。
提出 $645120$ 后在 $(q,r,s)=([K_7],[K_8],[K_9])$ 中依次是
$$
q+4r,\ -2q,\ -2q,\ -8r/3,\ q-28r/3+6s,\ -q-12r+6s.
$$
相加再乘 $-1/2$ 即(5)。

R434 已付这十列的 Q 像秩七、Q 核维三，current 像秩一；其中 current 核正是 $V_{51},V_{52}$ 两完整成本。故用十列付 Q，再用其中一个 Q 核付 current，不改变(5)的商类。最终两个新响应与既有三个成本形成整个五维 $\mathcal K_0$ 的完整成本基。其 **self 像是否仍有核** 尚未计算，不把五个成本维数称为五个 self 维数。

## 4. 只读已付 whole-Q 坐标，重放七 pivot

只消费 R316 主报告中的两个原 Q 列，不重新运行其 mapper：
run 43735872441，job 132878270740，
source ca186db057ed753abe565d0c3c2c8305278b5af7。

主报告 JSON+LF 为 61441 B，SHA
731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd；
完整日志为 182877 B，SHA
4d658489abd694f9f4cde2204aec9d23dc507d9ebae47168e42123cf4ff1288f。
同日志可能另有同 tag 的开发报告，必须按主报告 bytes/hash 选取，不能要求 tag 唯一。

旧列 index4/index5 的 nonpivot 必须分别为 8/9，完整 mixed SHA 必须分别为
61e1f2fa80e31b7605d246da44226cf02c5a82d727284e8e9eba5a185458d351、
cc177b7d2dd879b43ed58fcb8f2810344c58b648003ecb10a91681dcc53adb98。

Q 坐标为同一个 faithful $(T_9,\mathrm{Euler})$，沿 R434 的坐标 labels 重映射。下列七个原 pivot 已按原顺序归一：

| R434 record seq | pivot coordinate |
|---:|---:|
| 206 | 8 |
| 212 | 9 |
| 213 | 50 |
| 218 | 88 |
| 219 | 91 |
| 246 | 99 |
| 286 | 138 |

每个 pivot 的完整原十列组合从该 record 读取；其完整 Q 向量仅由对应已付 Q records 作线性组合。对于两个新的 RHS 只按这些已付 pivot 顺序作消元并保存全部系数/残差。这是新 RHS 的已付右逆应用，不重新求七维空间、kernel、pivot 或旧 rank。若残差不为零，停止为 input/source interface unresolved，完整输出已付身份和残差；不能擅增旧列或再跑旧研究。

原十个 Q records 为 seq
61,67,68,73,74,101,141,157,163,164。
坐标 labels 为 seq166。
所有 envelope 的 sequence、payload bytes/hash、完整 JSONL identity chain 按旧 run 验证。

## 5. 唯一 current 右逆原件

R434 run 43796872698 / job 133067569306 /
source 563defb46bc785295265c3f48fcad3fc8897c617。
完整原日志 1322512 B，SHA
1edd4dd8ac34e2a9fe6fc1cf7ae08dc2d91fa279c02e6c32365bff9830e013b1。
1020 个原记录的 JSONL 为 1170464 B / 
dd936dc713d3461cfbf2652c4e88c89ac4b918eb7949bb379f3b940d62cb8ec7，
identity chain 为
673061557c1b53e78bf300d18e11e510d091378ad3431e159f6049404cde5101。

唯一 current 校正列 $V_{707}$ 是 record seq707，payload SHA
729055c2e1075378e3ac5e771e24a6dd4ca824c8c4aa9fab800dd25eb7614e6b：
$$
\begin{aligned}
V_{707}={}&-\frac7{49920}B_YH_4+\frac7{109824}B_VH_5
+\frac{29}{2196480}B_TH_5-\frac{29}{3294720}B_LH_6\\
&+\frac{29}{3294720}B_UH_6+\frac{17}{2080}B_YJ_2
-\frac{576}{143}B_Y\chi_{40}+B_Y\chi_{104}.
\end{aligned}
\tag{6}
$$
原 $\mathscr C$ 唯二非零坐标为
$$
A_2^{[1]}=\frac{69}{4576},\qquad A_1^{[2]}=-\frac{69}{9152}.
$$
故
$$
Z_c=-\frac{9152}{69}V_{707}
\tag{7}
$$
满足 $A_1^{[2]}=1$、$A_2^{[1]}=-2$。其 whole-Q 零、所有原成本同权零均为已付输入；不重算这条列的 current。

对四个先已 E 零的成本 $W$，唯一新数记
$$
a(W)=A_1^{[2]}(\mathscr C(W)),\qquad \widehat W=W-a(W)Z_c .
\tag{8}
$$
完整权零 current 只占此一条线的结论来自 R462、R457 及原 $D=0$，而非此次有限采样。新代码仍输出四条真实 current 的全部三个矩重构，保 residual；它不重新计算旧 current 像或 39 行 rank。

## 6. 新 self 累计量及原左常数

统一从原 mixed 根取
$$
\Sigma_W(u)=W(u^2,0)=-4M_{-2,W}(u,u).
$$
用同一右锚 $I=-J$ 定义
$$
S_W^r(x)=p\,\Sigma_W'(x)-r\,\Sigma_W(x)+I(t\Sigma_W)(x),
\qquad (S_W^r)'=p\,\Sigma_W''.
\tag{9}
$$
真正左累计量为
$$
S_W^\ell(x)=S_W^r(x)+\Omega_W(u),\qquad
\Omega_W(u)=\int t\Sigma_W.
\tag{10}
$$
对两个响应补列及 $X_Y$，原 $\Omega$ 全部为零。对 $X_H$，
$$
\Omega_{X_H}=n_2
$$
是 R406 的完整十二项局部五次泛函，**不是 universal 零**。当前 R455/R464 的同一母四约束及其全部正仿射副本使 $n_2$ 准确零；因此只有在这个已付母类上，(9)直接等于所需左累计。输出必须保留(10)的这个来源/端常数，不能把响应的 $\Omega=0$ 套到全部正常成本。

对付 Q/current 的 $B_E\tau$ 校正，不重新映射旧 Q 或 current。直接消费 R434 已付 $(a,b,c)$ 原表，设
$$
h_\tau=(ar)'+bp,\quad w=q_E,
$$
则新 self 累计的完整 Green 表达式是
$$
2\{a(pw''-rw')+w h_\tau+uI(cw)\}.
\tag{11}
$$
它的导数为 $2p\{(aw'')'+bw'+I(cw)\}$；原左 flat collar 付积分常数。$w$ 的左二次尾和 $I(cw)$ 全保。两新 RHS 的 Q/current 校正使用同一成本组合的(11)，不能换另一组 self 代表。

## 7. 有序 3+2 的精确新读取接口

本次 current RHS 不能由 Ω 或 Q 反造。先把(9)、(11)的完整 one-color right words 正规化，之后才在真实不交 $u<v$ 上取 $[a^3b^2]S_{au+bv}^r$。

一个 right word 的 letter 顺序是由左向右的积分次序。每个局部 letter 在不交输入上只能全取 $u$ 或全取 $v$；混合 jets 的局部乘积为零。位于左包的 outer jets 全取 $u$，而一个有序 word 唯一可能的颜色分配是 $u$-prefix 接 $v$-suffix。仅保 $v$-suffix 的总 profile degree 为二；不作任何 profile 评价，不新增采样。

纯右 suffix 的单字为完整 signed 积分，其左常数是负的全积分。双字或其它闭 quadratic word 必须精确保留。单字的平方导数积分只通过真实 compact IBP 化简；与
$$
\mu_0=\int(v'')^2,\quad \mu_1=\int x(v'')^2,\quad
\mu_2=\int\{x^2(v'')^2+2(v')^2\}
$$
比较后，所有不在三矩 span 的项须逐项为零才授三矩读取。剩余闭双字或非三矩局部量一律输出并标 unresolved，不以形式余词非零授函数非成员。

(10)中的 $n_2$ 是局部五次，故其有序 $3+2$ 系数恒零。这是本读取不受 $X_H$ 左常数影响的准确原因。输出 current 使用 R433 的 $K/4$ 规范；self 输出使用完整 $K$，二者不可混倍数。

对每个新 current，完整三矩表达式再作 **仅 outer**
$$
t=r^2/(3p),\quad p\ne0
$$
代换；不微分 Af 身份，不替换积分 letter 中的 $t$，不删除高阶 outer jet。完整三矩 current 必须与(8)的唯一线重构相符，才继续其同一成本 self。

## 8. 新输出与停机边界

每个目标依次、立即输出：

1. 原成本展开、原 mixed 根及必要 input restoration 身份；
2. 两响应 RHS 的已付 Q pivot 应用系数及完整 residual；
3. 必需 current 的完整字表达式、三矩分解、唯一标量 $a(W)$、完整线重构差；
4. (8)的同一最终成本原标签展开；
5. 新完整 self 的 right words、(10)原左常数、完整 Af 代换；
6. local、nonlocal、higher-jet、$p$ 分母分别保留，完整来源和 Green 差证书。

全局部时，输出两个镜点 $u=h r,p=\pm s r$ 的完整符号多项式，$h,s,r>0$ 为实际镜点的归一参数。坐标是物理 $x$，不是擅移全局几何。实际左右点可再代 $x=\xi\pm b$；这一步是多项式恒等，不作已选 profile 的数值评价。

原 $V_{51},V_{52},\mathcal K_8$ 的完整已付 Af self 仅从 R443 records108、109、119 读取。它们的旧 rank 不重跑。若新四值没有完整 local 呈示，输出完整残词并停在精确接口；不能强压局部。若全局部，五个成本的完整镜对矩阵和两个目标即已明确，随后直接继续这两个新目标的小成员比较；本次不自动把 universal 符号非成员当固定母非成员，也不以未知镜点参数当自由实数。

## 9. 原输入、源闭包与预算

复用 R406 的只读静态 mixed 恢复方法和同 Γ normalization，增加 C4；复用 R126 原响应标签仅恢复(1)八列。响应原 mixed 与已存原 hash 逐一核同。新恢复数量准确为三静态 mixed、八响应 mixed；其工作单列为必要 input restoration，仍计入本次总资源。原 pure/旧完整 Q/旧 Ω/旧 rank 均执行零次。

复用冻结：
- R406 原 reader 及其 31 个源码依赖，source d47749f7289ba0965e912a0e0e026bc619ebd4cb；
- R434 完整 current/预算/字规范接口，source 563defb46bc785295265c3f48fcad3fc8897c617；
- R443 outer-only Af/已付 self 记录读取接口，source 9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac。

新 entry 为
scripts/literature_weight_zero_complete_self_currents.py，
request 为
computations/request-weight-zero-complete-self-currents.json。
运行参数只用 --request PATH --out PATH，纯标准库，不调用旧 main/science/development。源码/请求/workflow 的完整 SHA 闭包由根绑定；workflow 在运行前真实 pull 两库并读取双 README、私有根与 QUEUE。根独占 refs/调度；本代理不执行新研究。

建议硬上限：总科学（包括原日志读取、必要根恢复、新符号操作及失败）180秒、1024MiB、500000个总 primitive calls、300000个总 cache entries、8192 rational bits、80000 terms、5000000受监有理操作、2500000B数学stdout；所有 owner/fresh 的 primitive/cache **合计**受限。只读日志预算另固定16MiB/每份，读取时间单列且纳入同一180秒科学钟。无新开发 suite；必要原差证书属于四个新收缩自身。

使用 shared progress sink 和逐 record journal：任何 finite failure 都保已开始/已完成阶段、每条完成输出、实际 timing、RSS、primitive/cache/有理计费与所有 overshoot；不以未完成值冒零。stdout cap保既有已发记录及费用/指纹，不把整份报告替成一个错误字串。原日志与机器输出只在 runner 内存或临时目录及公开 stdout，不创建 Git blob、不挂树、不上传 artifact。

## 10. 明确不包含的结论

本合同不预言四新值局部、五 self 像维数、两镜成员或正字符消失；不把当前母的 $n_2=0$ 升为 universal 零。没有重做 R316 七维 Q、R434 32维 current、R443 38/49 self、R448 19镜像或 R452 特殊 $r=0$ 镜像。实际正锥、有限 C1 截面、全部内部根/全宽/全角色及原13规范，只能在新完整值之后按各自原合同继续，不能由这个 reader 或 signed 基直接推出。
