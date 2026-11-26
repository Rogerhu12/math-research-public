# 同父八轮分离的完整 SOC 首次真实接受及自身连续几何

2026-11-26，Astra-larger-e4e2a2bf-20261126。真实公开 [run45762076394/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394)，stage63、65、66。全部逐字命令、源与输入输出身份见[第6卷](2026-11-26-public-actions-45762076394-1-part-006.md)和[第7卷](2026-11-26-public-actions-45762076394-1-part-007.md)。本条只登记实际返回，不重做方向或继承其他场证书。

## 1. 实际方向与准确边界

完整 driver `1c87c624f29dd73c34998e2c87d8c0ce74c7b50ba7178aa3d04b29f112c2785a`，launcher `9c51346f9b2a7b5e473c4226cd76a5410f6171feb70c1d1125a32cc5a7215689`，实际 checkout `a54b554fe6514e196f3ddb3ea7836f9251ad1e47`。实际父 `2d3e053c0e49cdd238a5483137d4921c467437e1d4a7f28ce181bad9616a2b31`，新场 `7ebb5f42b29e0979f7a84a93fb8decb0b45ae8ec2f8c713bed820a8adb33d37b`。全7377正权径向行、2048全角/513代表点、全部原变量与H²母范数保持；physical/p4目标、epsilon .001、scale .05、旧192加5幅度行、4.2/.9/1.01预算、必要曲率门 .992/active-band .025均未放松。

| 量 | 父 | 实际末值 |
|---|---|---|
| 同一 moving-mean Phi | 0.00016727066158414496 | 0.0001392033999130046 |
| 正项 centered Phi | 0.00016695066158414502 | 0.00013888339991300467 |
| max relative Gram | 0.014179633163807326 | 0.014722916328831048 |
| damping μ | 0.01 | 0.005 |
| 永久曲率位置数 | 2741 | 2752 |
| 永久半径位置数 | 2735 | 2737 |

真实接受为 `complete_rows_soc`，alpha=1，第8轮；实际同目标下降 0.00002806726167114035。**最大度量误差上升，不能将平均损失下降写成uniform改善。** 本目标仍是moving mean，尚未成为README要求的同一固定g实际精化链。新场 `known_set_complete=true`，新增位置全部保留。

QP实际256次advance，状态 `iteration_limit`；末Pg=0.0006001557715460942，实际tolerance=1.4175363317709925e-9，reader实际比值 423379.4634358982；末活动面只有11 advances。J/J*=265/266。不能据总256步或此次接受宣称驻点，亦不能据末面11步断言固定面预条件失效。

最终必要点筛 product=0.9912526995388484，K=8.05481086124572，D点下界=4.102114527638314；幅度g_max=-0.045159801937189936，H=1.882104833137426，两筛均实际通过。点筛不是全域曲率或reach证书。

## 2. 八轮实际归因

每轮保持同一原x/d/fullpoint，独立读修正模型A*z和真实Phi、全曲率/幅度/完整记忆点；没有把上一修正点改成新父。实际身份依次为 `a8a6dbdcb6f361bf70b78ebbf4ca56352caf9a07477b679557bd447ff46413fa`、`c553adccc74b1b4d7128664b8e70164df38b7aa977a98f6a11ebc9edd6759c58`、`33d0755420c5dc1def510e31dabe2e4d5340dbb7788f869af3ae2d3284aaa7d1`。

| 轮 | 累计typed行 | 投影状态/扫数 | fixed-parent真实typed最大值 | 全曲率product | 真接受 |
|---|---|---|---|---|---|
| 1 | 199 | converged_numeric/18671 | -0.00007248841068513274 | 1.026677262130428 | false |
| 2 | 201 | sweep_limit_feasible/20000 | -0.00007226814640734807 | 1.0007864170287757 | false |
| 3 | 203 | sweep_limit_feasible/20000 | -0.00007226099064769864 | 0.9994353803800874 | false |
| 4 | 205 | sweep_limit_feasible/20000 | -0.0000721778873823834 | 0.9964926746139905 | false |
| 5 | 207 | sweep_limit_feasible/20000 | -0.0000721953912141188 | 0.9941646898197158 | false |
| 6 | 209 | converged_numeric/8434 | -0.00007217255207436921 | 0.9926726237654478 | false |
| 7 | 211 | converged_numeric/8111 | -0.00007210199126182174 | 0.992188978600765 | false |
| 8 | 213 | converged_numeric/7818 | -0.00007207612016170804 | 0.9912526995388484 | true |

各轮新增2行。1–7的唯一完整真实拒绝类别均为 `actual_curvature_filter_failed`；每轮实际幅度均通过、missing_checks均空。2–5的投影达到扫数预算但数值可行，明确 `minimum_norm_convergence_claimed=false`，不冒最小范数收敛。最终第8轮直接线性违约 1.8577194361817095e-14，修正相对原方向范数 0.014734133082851085；同父q0=0.000055188526612374165、qz=0.00004209574180837352。实际全曲率最坏位置在多轮间交换，说明本次只让已选typed行变负不足以通过全点筛；继续分离真实拒绝极值实际解决了这一次globalization问题，不证明所有后续方向必然成功。

全原197行保留，最终213行，单次预留容量237；实际used bytes 2276106072、capacity bytes 2532568728、allocated disk 2276204544。每轮完整模型共8次J，全部实际使用行字节 6432938288；主报告all-row cache字段 6689400944另列，不能混同预留/使用/磁盘量。峰值RSS 3132072 KiB；stage63实际 1137.7218459739997秒，exit0，无摘要缺项或缺失输出。

## 3. 该新场自己的完整 first

stage66直接读取上述7ebb新场，source `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225`，checkout `f0dbc7cb89cd103834999d4718d81c2e0309b391`，model `4c8e450615a63136013110568207903624d070aa77b5c0b791a079fcbee54b82`。完整922胞、全角、准确帽、镜反射与完整参考尾覆盖，complete_scope=true、embedding_certified=true。

| 连续量 | 实际界 |
|---|---|
| D上界 | 4.124124731119599 |
| 固定witness到整像距离下界 | 0.9385645470439958 |
| 未加标记body的held/D下界 | 0.2275790884698093 |
| 加权support下界 | 0.30163322855113867 |
| E下界 | 0.8401404313139432 |
| 法向平方下界 | 0.006851889785468466 |
| core rho下界 | 0.15266899486241478 |

准确H=`8476246625189921/4503599627370496`，width=`3602879701896397/72057594037927936`，beta=`1/4`；R盒为 `564734175386577761774707/1000000000000000000000000` 至 `282367087693515366508543/500000000000000000000000`。节点 `06e56f248db23c20a7f91c32861cd64daf51706ce06bf74aeeb5ee6070ef3734`，参考载体 `3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8`。reader内部 56.62654934999955秒，总 61.55287895000038秒，exit0，无摘要缺项/缺失输出。marker_certified=false、nonplanarity_certified=false；完整K/四标记/reach、全域metric和固定g求解精化尚未付，未用旧场证书填入。

## 4. 可复现身份与继续执行

| 实际输出 | bytes | SHA256 |
|---|---|---|
| mean-metric-design-amplitude-separated-SOC-v2-first/report.json | 46498415 | `749fc0a31661e111f2621619b45da25bf25fe0a53a6feca348c831aa1e221821` |
| mean-metric-design-amplitude-separated-SOC-v2-first/final.npz | 10375742 | `7ebb5f42b29e0979f7a84a93fb8decb0b45ae8ec2f8c713bed820a8adb33d37b` |
| mean-metric-design-amplitude-separated-SOC-v2-first/exact-tail-lift-profiles.json | 11282 | `0a8bc1ed3763722ecaf9486a05da4e51979807b915b7aa635c807a5cbcbef6d4` |
| mean-metric-design-amplitude-separated-SOC-v2-first/exact-tail-lift-profiles.npz | 150838 | `3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8` |
| mean-metric-design-amplitude-separated-SOC-v2-first-command.json | 54801 | `c57f78c109e759155c5786abf61dd03fcf2f31ac04e56dbcb5e5ddc9639031a0` |
| mean-metric-design-amplitude-separated-SOC-v2-first-inputs/complete-parent-positions.json | 176123 | `733ff6c8552bdb4a9a89b990e5b530486e6af749b7ca248f0a00425d7f1e0302` |
| postprocess/held-amplitude-fixed-parent-separated-SOC-256-first-summary.json | 492921 | `48814a3d838d103dd9a18ab887371cc144ed29931c40a1d0ba24189f7a36a247` |
| mean-metric-design-amplitude-separated-SOC-v2-first-geometry/first.json | 1032241 | `449a672f86253f14e8866d98464a8a0704b4dc0d2edb5f6bf89bc1dcf96fb364` |

纯归因source `c74e66265fc9b231ff32c2873c21a9ef27c8735af84a736b31671ffa25363f7d`，checkout `b7386965014e9b4161710619f104ddd324973841`，实际 6.183340887999293秒、科学数组读取0。全部raw/完整逐点报告只留runner，不上传Git/Release/artifact。参数和实际命令在上述两卷可完整重建。

继续已排同一固定deep目标的真实2×256/完整多轮SOC，先按其真实返回选择细化；保留本7ebb父的全部2752/2737地点，作为真实材料Haar积分与新固定目标的一个已读输入。Haar目标必须由该父完整重新积分，旧physical-mean Phi不可跨目标比较。尚未完成README，不停在本条方向记录。
