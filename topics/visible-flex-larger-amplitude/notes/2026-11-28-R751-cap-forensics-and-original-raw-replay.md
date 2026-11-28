# R751 原曲率矛盾的完整帽测量与原调用顺序重算

状态：**数值证据；原峰值尚未重现，矛盾未解，不作为全曲率或 reach 证明。** 原完整证明和首次测量见[原记录](2026-11-28-R751-curvature-mixed-atlas-complete-launch.md)。本记录不改写原值，也不将新的较小值替代原值。

## 实际来源

原测量 run 46150384106/1、job 140995509084，源提交 5aa9bd7554e6363a71e673157f7f83644e80358f。原全 raw 113197392B，SHA-256 69bca3cab9ff1cc12c47c20aca55d7526aeeb3979e3016554244c3565c80cefc，仅 runner；完整有限原结论已在原记录和固定 Git 保存。

追加真正执行 run 46151602924/1、job 140999229999，官方状态 success；源/触发/本次真实 README pull 均 72f20474143e769506f86c3760b6eae3bc114655。脚本 forensic_r751_original_caps.py 6411B / SHA-256 6ae2a752dc2cbae64a1520803d2d5fe0f9590f31f1204db7eee3ef08d05f99fc / Git 1ec218cb0be0ec3cbd6cb9d105e6e9dd9544b18b，workflow visible-larger-r751-cap-forensics.yml 3429B / SHA-256 2661a33e3f8c6b77cd802033230311e63fc877e041942283f0ec658d7822299e / Git 3c5fcc0d8c075133d3af759b45318614c228826f。参数为原三层 (48,12,16)、(96,24,24)、(192,48,32)，七相位 0,.4,.8,.9,1,1.2,π/2，两整帽；42 个整域返回均完整读取。

[全部原有限返回](https://github.com/Rogerhu12/math-research-public/blob/6911c06ce5a90b0cd03232a9a42d0f19fc44e63b/topics/visible-flex-larger-amplitude/notes/r751-actual-curvature-mixed-atlas-46151602924-1.json)：63709B / SHA-256 bc7ebd9fb3ea732b047f654e34dce9d5bb267507ccfce09313084e85f5389b79 / Git c80709afcf8d0172eb66eeaff9f4ff624432fd66。不重复保存可重算数组；本次派生 raw 12387984B / SHA-256 71c42db182b43c3a14b33ff21e4f3d6b3925b3785593d12f322174bae43dda94，未上传。

## 已经实际返回的区别

本次首先调用未旋转帽六jet，再调用世界坐标六jet；对同一次新生成帽，比较工作坐标主曲率、切向 SVD 正交化以及物理 Cartesian graph 的真链式六jet。

最细层终相的两帽工作坐标峰分别 3.9124247373725742 和 2.610066448136576；共同参数 s=6.306512161137539、v=.5833333333333334。对应正帽 SVD 主曲率 [-3.9124247373736365,1.0864381208353115]，Cartesian 绝对峰 3.912424737373705；负帽 SVD [-.7244571097369696,2.610066448137119]，Cartesian 2.6100664481372937。切向条件数 108250.64763406168 / 108295.85019462477，面积 .1138194988699648 / .1137935711258316。所有 42 行 graph 一阶链差不超过 1.38778e−17，二阶链差不超过 1.7763568394002505e−14。

这仍没有解释原最细层终相的 370.7885676392032 / 247.3521463740392。原最细层相位 .8 的 6.363562799666703 / 4.242595823333106、相位 .9 的 7.4444192190485925 / 4.963612557864718、相位 1 的 90.6303755467354 / 60.42026189552773、相位 1.2 的 95.68714964470584 / 63.80502673537893 也保持原样。本次没有定位原 raw 上的峰，不得称为原峰的 SVD 复核，更不能先归因为舍入误差。原全帽相对度量误差 8809.789388290248 仍未付。

## 立即继续的原入口完整重算

下一公开工作直接运行未改动 measure_r751_closed_mixed_atlas.py，保留全部原图、三层、七相位及原调用顺序；对其原始 raw 按 13 个图块的原顺序完整逐字节遍历，要求遍历总字节等于全文件，比较全 raw SHA-256。对每个真实帽块在磁盘值上计算原 Boolean 展平表达式及未展平表达式，保两种峰的地址、原报告值、全帽 raw 身份和再次直接生成身份；在实际原峰处计算物理 graph，最细终相两帽再交 SVD 和全部六jet。原程序、原值、原记录均不变。新的 run/job/自然返回尚未知，触发不作成功。

| 文件 | bytes | SHA-256 | Git blob |
|---|---:|---|---|
| scripts/resume_20261126/r751_curvature_mixed_closed_two_jets.py | 13877 | 08416719155ce0d4a689410cf7ac5e9995f606358c5730298cb723d4eeb53e07 | 53f39fc18e4595102a7277a3008c2ad07325da88 |
| scripts/resume_20261126/replay_r751_whole_raw_cap_costs.py | 6699 | c5748ee700687c833ce4c443d212303c3417d5d49b2d72b7153133ecb09ba460 | 1db5d3c639e4bc444b48cf1d548b65c741bf767a |
| .github/workflows/visible-larger-r751-raw-cap-replay.yml | 3524 | 20a8fc3655e315a36b91e868169231b512c936e696f4d082eb58fdf6fcf0cc85 | 84a55fcf95836e430dc9dcbaf89171365ee48367 |

公开 workflow 使用 numpy 2.2.6、原60分钟上限，无人为缩小原科学域；输入复用首次完整测量和 forensic 两原脚本及其提交的父源。结论仅根据真正返回填写。改 .github/workflows/visible-larger-r751-raw-cap-replay.yml 是为本课题追查真实矛盾。

## 原入口复现已经自然返回；差异定位到同次算子调用

run 46153716771/1、job141005656948 官方success；source/trigger/真实README pull均33903089f2ac51aac852c3c51c257035a6f77271。完整[原返回](https://github.com/Rogerhu12/math-research-public/blob/2070af6c745df4f1703f87d93cab789f23dfb50b/topics/visible-flex-larger-amplitude/notes/r751-actual-curvature-mixed-atlas-46153716771-1.json) 37272B / SHA-256 4cb33726d3462f9ad1144827bcbd22ba983284f2b7562c72bd4769daa61f8d12 / Git b17309940478849efea0df2537c051012f2c282f。未改原程序完整raw为113197392B / SHA-256 22358869d9a99185ec3259074a3c36eccdb73197a642f3dc3a764be2fc52bf54；它与原69bca3...全文件不逐字相同，不能称重生了原raw。

但这次原measure在新的真实raw上又返回最细末相370.7885676392034 /247.35214637403942，复现了原高数值。42/42完整帽块与本次各自直接重调的六jet逐字相同（raw_vs_fresh_max=0）；同一磁盘帽块外部重复原字面展平公式却给3.9124247373725742 /2.610066448136576。最细层所有六个非零相位、两帽共12行有此差异；另30行一致。这次已经将冲突局限到同次原函数与外部计算之间，不能说物理帽场/调用缓存不同解释了它。

外部低峰坐标s6.306512161137539/v.5833333333333334的SVD与Cartesian仍一致；这些是**外部低峰**的六jet和曲率，尚不是原内部高峰的地址。原完整全帽relative Gram8809.789388290248不变；未付全g、未凭此修复reach证明。

下一公开脚本原封运行整个3×7×9及全部17点窄域，再对42帽同一原raw调用原measure，用sys.settrace只捕获原内层op的两次return。记录实际b/g/d/tr/disc/返回向量全身份、内部真正argmax、全部外部同式比较；在内部原高峰处读世界六jet、Cartesian链与SVD，比较叉积面积平方、Gram相减行列式、SVD奇异值乘积平方和数组对齐。Python字节码亦留。原算术、预算和科学场不改，不能先把差异归因于舍入或已修复。

trace源 scripts/resume_20261126/trace_r751_original_cap_operator.py 7091B / SHA-256 88b5f63728374bc9d24f34a3725c4500361f3ddd5b7cc96157a73eb91e527ec4 / Git 73a7366fed978ef5efeb1c9a908679aa668fa6da；workflow .github/workflows/visible-larger-r751-trace-cap-operator.yml 3565B / SHA-256 fab0851dbd7066f7c1bc3c7be3276b03cae7cb92b7c6ea1eeccab3e15670b5e1 / Git eb7df04003bfea4b44b8e768f970e198e65c2a40。完整小结按固定原replay报告SHA锁定来源；raw仅runner。实际新run和结论待自然返回。修改课题外该workflow只为定位真实原算子冲突。
