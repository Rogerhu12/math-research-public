# 实际 Miller 长链的全54方向恢复检查点

日期：2026-11-12；qc_global。完整结果已登记R151；本文件保留历史恢复记录，现行入口见末节。

## 已完成与正在运行

原标量链已经实际完成20位、28个 AddFlip，滚动文件为 /tmp/p41_poincare_miller47_rolling.json.gz，SHA256 为 678303cd235882c18a7a75b2c339465adbae45aec5237e20b2432be2b1a38933。它已安全停止，未覆盖；先前已发布的首5位快照也保留。

为避免在完成304位后另跑一次同样的大乘法，新的驱动 p41_poincare_miller_jets47.py 在同一链上同时保存全部54个独立移动点方向的三阶对数范数展开，即162个 $R_2$ 系数。它复用原始实际 AddFlip 算法、随机种子及主截面，逐步检查每个点的全部哈希和 R121 已发布长链相同；在前20位还逐项核对旧标量链的实际主函数范数及纤维坐标。

新运行的滚动路径是 /tmp/p41_poincare_miller_jets47_rolling.json.gz，每5位原子写入。日志是 /tmp/serre-p41-poincare-miller-jets47.log。本记录写成时已完成25位、37步并继续推进；该次固定快照 SHA256 为 ff8f4cb985083e7e24b54d435de1bde50eb8adae25ab621350a6616280d65b15，纤维坐标为1529710。根代理保存时可复制更新的完整原子文件，并另记其准确位数和 SHA。

首版源码 SHA256 为 6d1705c8f4ef0d0314637598dbab8517793590aae1935b65de3a498fb55ba01d。下述45位安全升级后的现行源码 SHA256 为 ad632188a7fca0c274adfe3d8b3946e6db58a9f361d3fb79abc06ff9c26aab5c。完整链未结束以前，不得把文件中的中间坐标称为最终非形式点高度。

## 同一框架和准确递推

全部第二变量仍使用 R141/R145 的新54点 Abel 族
$$A_2(Q)=Z_2(t(Q))-Z_2.$$
第一变量的起始代表是 R112 真正的 $B=B_{-4}$。旧恢复记录中的实际底除子、整数 $m$、负点规范、主截面和终点框架变换保持不变。

对实际截面 $f\in H^0(3\mathcal L)$，若它实现负和
$$R=-(P+Q),\qquad \operatorname{div}(f)=E_P+E_Q+E_R,$$
则主函数为 $\psi=f/f_0^3$，纤维坐标递推为
$$u_R=(u_Pu_Q\operatorname{Norm}_{A_2}\psi)^{-1}.$$
每步仍用54个实际移动点的值直接计算这个标量范数。

此外，若一个截面在第 $j$ 个移动点的展开为
$$s_j(t)=s_{j,0}(1+r_1t+r_2t^2+r_3t^3+\cdots),$$
则
$$
\log(s_j(t)/s_j(0))
=r_1t+(r_2-r_1^2/2)t^2+
(r_3-r_1r_2+r_1^3/3)t^3+O(t^4).
$$
从 $k\mathcal L$ 截面中扣除 $k$ 倍底截面的展开，得到真正主函数的三阶对数范数。54个点的范数相乘，因此对数是各点贡献之和，不需要存储交叉点的多变量单项式。按上述负和规则逐项递推，得到完整 $54\times3$ 系数矩阵。

每一步都把这些系数代入 R145 的真实形式点参数，独立检查所得对数等于直接54点范数的对数。所有值均在模 $47^4$ 的准确有限环中计算。

## 完整链终点将产生的对象

完成时的实际第一变量点应与 R121 完整检查点逐项相同。驱动器再使用已验证的真实终点主函数搬到 R141/R145 的新第一变量框架。该终点变换的范数已经独立算得2703817，旧恢复记录及 endpoint 小证书仍有效。

完整输出将包括指定非形式第一变量、形式第二变量的实际局部 Poincaré 值，以及模 $47^3$ 的54个真实 Lie 导数。对导数的精度说明如下：R140 的高阶项总次数至少四，固定第一变量 $Y\in47J$、第二变量在零点求一次导数后，剩余每项至少含 $47^3$。双扩张的同一框架和 R141 的修正矩阵始终保留。

这些导数依赖明确的代数纤维选择；它们不自动等于全局自高度系数，也不替代 R148 全局规范截面的纤维搬运。最终 R151 必须继续区分这两类对象。

## 恢复方式

先按已发布的 2026-11-12-qc-miller-first-variable-recovery.md 重建 R145 的必要原始 Abel、三阶截面、指数及 Hessian 数据；输入文件的全部准确 SHA 已保存在新检查点中。将根代理保存的完整快照复制为新 rolling 路径，再运行：

~~~
python -u /tmp/p41_poincare_miller_jets47.py \
  --script-dir /workspace/scratch/64b49fd2bdbb/math-research/topics/serre-uniformity/scripts \
  --checkpoint /tmp/p41_poincare_miller_jets47_rolling.json.gz
~~~

若源码已保存到仓库 scripts，替换第一行的脚本路径即可。旧20位标量前缀丢失时可以省去其额外比较；R121 原始长链和每步直接范数/三阶展开相等的主验证仍执行。不要把新 rolling 文件重命名成旧标量文件，两者状态字段不同。

所有 NumPy int64 点乘仍使用 R117/R141 已核准的整行累加界；新增的54项对数求和只有 $54(47^4-1)$，远低于64位范围。没有为速度改变已发布长链的随机或主元次序。

## 45位处升级：保留真正的主函数 SLP

在45位、67个 AddFlip 的准确原子检查点暂停后，驱动器增加了每一步325维三次截面系数的保存，随后从同一检查点继续。未丢失任何完整位；旧检查点另存 /tmp/p41_poincare_miller_jets47_before_slp_45bits.json.gz，132798字节，SHA256 为 aa404346d824f6c90403507babcd7aab9520fa6ad5ce8fc278528c70c585e387。

从第68个 AddFlip 起，字段 principal_section_coefficients 保存真正的 $325\times1$ 个 $R_2$ 系数，原有 principal_coefficient_sha256 仍保留。前67步原先只有这个准确哈希，另用 p41_miller_slp_prefix47.py 重放到45位，逐步比对全部点哈希和全部主截面哈希，补齐这些系数。其独立原子文件是 /tmp/p41_poincare_miller_slp_prefix47_rolling.json.gz；日志是 /tmp/serre-p41-miller-slp-prefix47.log。前缀完成后可以将67份系数合入主链的稳定检查点，避免保存重复的旧状态。

这份 SLP 不依赖当前第二变量。对任何后续适当不交的实际除子，可以重新计算它的函数范数，而无需重做304位群运算。其符号规范准确为
$$
\operatorname{div}F_n=nA_B-A_n,\qquad
F_{-(n+m)}=(F_nF_m\psi)^{-1}.
$$
负点初值是 $(a/f_0^2)^{-1}$，终点框架改变后 $F_{\rm new}=F_{\rm old}/g_{\rm tr}$。因此它直接给 R154 所用的 $mA_B-A_Y$ 主函数，不存在隐含的逆号。

前缀恢复命令：

~~~
python -u scripts/p41_miller_slp_prefix47.py \
  --script-dir scripts \
  --reference /tmp/p41_poincare_miller_jets47_before_slp_45bits.json.gz \
  --checkpoint /tmp/p41_poincare_miller_slp_prefix47_rolling.json.gz
~~~

全部 SLP 是实际 Miller 证明数据，预计压缩后约1MB；它不是需要入库的大型目标评价矩阵。

## 补记：110 位时补齐全部主截面系数

在 110 位、165 步的安全检查点暂停主链，已把独立补重放得到的
前 45 位、67 步真实 `325×1` 三次截面系数并入原子 rolling。
每一条的系数 SHA、Jacobian 点 SHA、操作、位数、符号与全部记录的秩
均与原已保存记录一致；补重放不是另一次 304 位长乘。

补重放完整文件 `/tmp/p41_poincare_miller_slp_prefix47_rolling.json.gz`：
294528 bytes，SHA256
`b5f5fbf03a9a339cc2775a29acef0c2574055d08a4503523075018164d7325b8`。
合并后 110 位 rolling：563736 bytes，SHA256
`be8e694fcf63200e77e8f4f3c5a27cff2cf1d73c3afb3e5ff9ae4f102aa7da33`。
此时第 1–165 步全部有 `principal_section_coefficients`；后续由同一驱动
自动保留全部系数。源码仍为
`ad632188a7fca0c274adfe3d8b3946e6db58a9f361d3fb79abc06ff9c26aab5c`。
主链已按上文原命令从 110 位继续。该补记只报告已完成的恢复验证，
不把未结束的长乘或尚未计算的全局高度标为完成。

## 110位批次仓库固定恢复入口

当前完整快照为 scripts/data/p41_poincare_miller_jets47_saved.json.gz：110位、165步，563736字节，SHA256 be8e694fcf63200e77e8f4f3c5a27cff2cf1d73c3afb3e5ff9ae4f102aa7da33。已包含所有165步主截面系数；恢复主链无须再跑前45位补系数。早前45位参考和20位前缀仍保留作历史记录。

本批另外保存 scripts/data/p41_miller_cm_units47_checkpoint.json.gz（26个真实CM支撑、165步中46步至少一处非单位）及 p41_miller_canonical_norms47_checkpoint.json.gz（固定Kg、165步中28步非单位）。估值4只表示至少4；这些是尚待整盘消因子的检查点，不是已完成的全链单位部或高度。Kg长度106限制代数的compact及可重建源码同时保存；全部199/325乘法恒等式和一项整数resultant/行列式范数吻合，R160的最终结果另行登记。

## 200位302步历史恢复记录

2026-11-12 23:50 Asia/Taipei 后保存的完整原子快照为 scripts/data/p41_poincare_miller_jets47_saved.json.gz，200位、302步，929124字节，SHA256 a9b1cac05875dae642964c7d123d478e2c1f289646ef573c40bdcb07f4a62aa4。全部302条真实主截面SLP齐全；主链未暂停，继续原rolling。恢复用此文件，无需重跑已完成位。

R160所绑定的110位165步原字节另外保存在 scripts/data/p41_miller_all54_slp110_fixed.json.gz，SHA仍 be8e694fcf63200e77e8f4f3c5a27cff2cf1d73c3afb3e5ff9ae4f102aa7da33。恢复R160固定证书时复制这一文件到同名/tmp路径；不能用后续文件冒充165步输入。完整链、全局高度与QC共同根仍未完成。

## 历史恢复入口：270位403步

2026-11-13 00:22 Asia/Taipei 保存主链原子前缀到 scripts/data/p41_poincare_miller_jets47_saved.json.gz：270位、403步，1198431字节，SHA256 b938a9b6aebbe3cfe0c8506dc9b71c24591a13677f94ddd04dfff7894c68e945。全部403步真实主截面系数齐全，当前点SHA ad1db9adb36d83e7ea2c86bb46467983ee2d8a6900e45c0fe8a0c285bd42fa57。恢复此入口可继续剩余34位；主运行未中断。R160仍用另存的110位固定输入。两条CM类长链的独立恢复入口见 notes/2026-11-12-qc-cm12-cm7-miller-recovery.md。


## 现行入口：完整304位454步，勿重跑群乘

2026-11-13 已完成全部实际主函数和范数，见 [R151](../results/R151-complete-miller-local-connection-and-cm-norms.md)。现行 scripts/data/p41_poincare_miller_jets47_saved.json.gz 为1340024字节，SHA256 2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed。全部454步325维系数、端点换框、三阶范数及54个Lie导数齐全。26CM和完整106次典范范数已完成；最终小证书p41_miller_completion47_compact.json.gz保存指定局部值1730352mod47⁴和实际F(Du)/F(Dc7)。

原驱动两次OOM后从295位原子点恢复，finisher只将保存频率改为每位并释放闲置JSON；逐步仍与R121点链和原系数哈希完全相同。R160固定110位165步输入保留原字节，不能用完整文件替换其绑定输入。两条CM链继续独立运行；后续范数复算重放此完整SLP，不再做304位群乘。
