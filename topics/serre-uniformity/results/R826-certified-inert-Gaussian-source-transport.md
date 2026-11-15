# R826 实际惰性 Gaussian 源运输：六个单位系数与两个零通道

2026-11-15。状态：**固定八项准确运输已在公开 Actions 完整成功。**
本条没有计算八个 companion theta 的实际 CM 值，也没有证明其指定和非零。

## 1. 已得的实际简化

消费 [GC 的原四角色/八oldform分解](../notes/2026-11-15-sigma-inert-Gaussian-rayclass-source.md)
及 [R826 原 companion CM 比较](R826-original-inert-companion-theta-CM-pairing.md)。
原源的八列按次序为
$F_3(t),F_3(t^2),F_3(t^4),F_7(t),F_7(t^2),F_7(t^4),G_1(t),G_5(t)$。

在原基 $(S,F,H,R,J,G)$ 和同一 Miller/Heisenberg 归一中，真实结果是：

- $G_1,G_5$ 两列在 FG 和 HJ 两个条目中都准确为零。
- $F_3,F_7$ 各自的三个 oldform 列，在 FG 和 HJ 中都非零。
- 这十二个非零条目在所有有理素数 $p\ge41$ 上的每个素点均为单位。
- 完整八维源矩阵和八维运输矩阵在这些素点也均可逆。

因此 R826 的原未筛交替卷积准确缩为六项：
$$
\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j
=-\frac{120c^2}{d_0}
 \sum_{\substack{b=3,7\\d=1,2,4}}
 \kappa_{b,d}\,\mathscr C_{b,d,p}(P_0),
\qquad p=6N+5,\quad p\equiv11\pmod {12}.
\tag{826C.1}
$$
这里 $\mathscr C_{b,d,p}$ 仍是 R826 的原权 $p-5$ 截面，已经包含
$d^{p-7}$；$\kappa_{b,d}$ 是原 $\widehat U M_{b,d}\widehat U^t$ 的 FG 条目。
公共 $c^2$、$d_0^{12}=-432$、原相位及同一 tame 点没有改变。

(826C.1) 的六个系数是单位，并不排除六个未知 CM 值的相消。
尤其不能将两个零运输系数误写成对应 companion theta 的 CM 值已经为零。

## 2. 真实准确分母与 Norm

计算字段为
$$
K_*=\mathbf Q(\alpha,\sqrt3,i,\sqrt2),\qquad \alpha^3=4,
$$
次数24。输出使用
$\sqrt2^{\,d}\alpha^a i^b\sqrt3^{\,c}$，
顺序 $d<2,a<3,b<2,c<2$。
下表中的 $D$ 是这一整幂基上实际清分母整数，Norm 指
$N_{K_*/\mathbf Q}(D\kappa)$，不是省略分母后的原值 Norm。
$F_3,F_7$ 对应列分别准确求得相同的这组分母和 Norm。

| 原条目 | oldform指数 | 实际D | 清分母整Norm |
|---|---:|---:|---|
| FG，F3及F7 | 1 | 968 | $2^{68}3^{30}11^{40}$ |
| FG，F3及F7 | 2 | 121 | $2^{92}3^{30}11^{40}$ |
| FG，F3及F7 | 4 | 121 | $2^{188}3^{30}11^{40}$ |
| HJ，F3及F7 | 1 | 484 | $2^{40}3^{30}11^{40}$ |
| HJ，F3及F7 | 2 | 121 | $2^{88}3^{30}11^{40}$ |
| HJ，F3及F7 | 4 | 121 | $2^{184}3^{30}11^{40}$ |
| FG/HJ，G1及G5 | 1 | 1 | $0$ |

这些值来自完整原字段的24维乘法矩阵 determinant。
对于 $p\ge41$，表中 $D$ 和非零整Norm均为 $p$ 单位。
整幂基的每个基元是代数整数，所以每个非零条目及其逆都在各个 $p$ 上素点整；
这给上述全允许素数的单位结论，没有做任何 $p$ 扫描。

两个完整八维矩阵的实际证书为：

| 原矩阵 | 实际清分母D | 实际整Norm或determinant |
|---|---:|---|
| 原EO源基矩阵 | 1 | determinant准确为 $-8192$；整Norm为 $2^{312}$ |
| 原EO运输矩阵 | $11^{16}=45949729863572161$ | 整Norm为 $2^{600}3^{432}11^{320}$ |

源基的行是 $(r,s)$、$r=0,1,2,3$、$s=1,2$。
运输矩阵的行是
$(S,J),(S,G),(F,J),(F,G),(H,J),(H,G),(R,J),(R,G)$。
所有列均按第一节的八标签次序，未转置行列或删掉一个零通道。

## 3. 实际运行与来源

运行：
[43725592504](https://github.com/Rogerhu12/math-research-public/actions/runs/43725592504)，
job132846716428，attempt1，最终 success。
source commit 为
d3a4216875ffde37005c74a8cf27687e631d935a。
数学步骤、完整输出上传及最终 verify 都实际完成。

| 原文件 | SHA256 |
|---|---|
| core sigma_inert_cm_source_transport.py | 70e565af2b00f2ad7a58f555bffd177f7a277d8a8c01dd49b6f6dde26d25de38 |
| wrapper sigma_public_inert_cm_source_transport.py | 2d61eb039457bb9dd4b0de99fd91631a0489dca1acb35706c744776e4a67ff3a |
| method | 013810fb3e6ec845151d7d9dba96c86f7465755e249bd406901b6b6ead8c9524 |
| request | ef5762030395fe20d09f755f6a6fc9198d59b59d4a6c45424737756afe2bbac0 |
| workflow | 503d8890da99fc1f270e92a0fb0a5e6292f176db83303b8f368a67c40087d566 |

原 R812 core 为
e7bac15678e6d0d30a30e54edd41a2d34a053b766da97efa7771278827e87ab2。
原R812、IH、GC全文的固定SHA也由request逐项绑定并在运行前核对。

Sage实际版本10.6；官方版本镜像此次真实digest为
sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。
数学容器网络关闭、源码只读。环境与source metadata准确记录为本公开仓库的push事件。

原R812输出没有保存完整U条目，故本次恢复必要的6×6原Uhat。
旧六个split Frobenius案例、旧Theta5、sigma高阶jet和任何素数窗口均未重跑。
本次实际新增的是36特征恒等、八个源/运输与其Norm；
旧已登记结论没有被冒称新计算。

## 4. 完整输出与只读核验范围

新的准确产物已保存：

- 原Uhat完整6×6；
- 原EO源矩阵完整8×8；
- 原EO运输矩阵完整8×8；
- 八列FG/HJ的全部24有理坐标、准确分母、整Norm和零标记；
- 所有行列标签、字段幂基次序、原规范主元及共同尺度说明。

后继直接读取这些已成矩阵，不再次恢复U。
本次canonical数学JSON为39280字节，SHA256
916e1b951a5acc6c375477ea13078d27a088ffcebac66ab76abf7a91676836a3。
完整job日志已实际读取；从该日志解析准确JSON并重新计算canonical SHA，
与core的RESULT_SHA256及最终verify回执完全相同。
源metadata、Sage版本、八标签、两类零列及上表全部真实证书均已读取。

公开wrapper的最终verify实际逐文件检查完整manifest中的bytes/SHA、
源请求、完整JSON、全部矩阵形状和24坐标，以及源commit/core metadata，
并检查清单覆盖全部输出文件；该步骤success。
这不是在本地重新计算矩阵或Norm。

artifact为
[14165618753](https://github.com/Rogerhu12/math-research-public/actions/runs/43725592504/artifacts/14165618753)，
实际17813字节，过期时间2026-11-16 14:40:58 UTC。
GitHub artifact响应及上传日志一致给ZIP SHA256
7f0bd3bd71241a68a520036b07403b8c354f7920b913898c7d695544a6b56812。
本次没有在断连环境中重新下载/独立哈希整个ZIP；
不能把平台已报digest称为本地独立archive核验。

## 5. 仍然明确开放的量

R826 的六项实际 CM 和是否非零，仍待证明。
全八矩阵可逆、六个FG系数单位、全局companion theta首项非零，
都不单独决定这个点的指定和。

即使该未筛和非零，原目标仍需同一个primitive且Legendre可见标签：
$P_{6i+6}(1/s)f_i g_{N-1-i}\ne0$。
本条没有加入这两个投影，没有给高度jet或有限Bézout，
也没有达到主Serre一致性完成标准。

可重算的完整坐标、机器JSON和raw仅在上述一日active artifact继续传递；
Git保留本解释、脚本、固定参数和真实run/SHA。
