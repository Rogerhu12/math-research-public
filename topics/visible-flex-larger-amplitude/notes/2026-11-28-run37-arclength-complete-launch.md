# 37 — 真弧长角与有限弯盘肩的完整新求解

会话 Astra-larger-e4e2a2bf-20261126。完整[六件源参及启动manifest](../computations/run37-complete-disk-arclength-source-and-launch-delivery.json)、[请求](../computations/run37-bent-disk-arclength-request.json)和公开workflow同时入main。本次准备时实际run、point、目标、科学返回均未知。33–35原完整变量、预算及自己的后继责任不变；36的完整八阶段失败已登记，不重作新结论。

## 新目标与真实完整初场

对实际肩C(s,θ)，w=|Cθ|、T=Cθ/w、q=Cs·T、V=Cs−qT，P为w的角均值。h=T·Csθ−w P_s/P的完整周期原函数Ih在反射对称下取奇函数，b=q−Ih。真实弧长角的三个Gram为 |V|²+b²、P b、P²；整个环的度量轴对称等价于 |V|²仅随s而变且b=0。设计同时放开两径向函数E(s)与P(s)，不再强制原材料角本身等弧长或E恒1。程序中的均值和原函数使用明确有限角FFT，连Nyquist处理、全部正反变分保全；全角准确原函数的费用仍待付。

新底场直接评价真弯盘D(r(s)cosθ,r(s)sinθ)的全部径向、角向及混合六jet，r=1+.15 tanh(s/.15)，再以完整两端Hermite权衔接镜面末环。B样条/Fourier控制保左端全二jet与右端镜面二jet，末环横向位置与加速度仍自由。没有拿选定一条法截线替代完整肩。四个实际候选为 γ=.44,H=.39的原stage05投影、γ=.32,H=.34的原stage04投影、γ=.38,H=.37的新底场、水平H=.17的R740椭圆投影。源场换γ/H或有限表示后其原几何证明不自动保留。

每个候选完整6span/m10、25×96训练/61×384错位核查，90评估/100 LSMR。所选者两设计级10/m14、37×144/83×512、100/120与12/m18、45×192/101×640、100/150。随后固定所选fine真实系数和640角定义的E(s)、P(s)函数，在每个实际s完整重算，不作径向插值。两级同目标为12/m20、49×192/109×640、110/160与18/m24、61×256/131×768、120/180，固定目标257×2探针SHA及source point均记录。全部body/witness/面积/8方向曲率原费用保，加入真实法向速度下限和相对镜面内中心的外法支撑费用；不是独立准入门。

未标记盘的支撑公式和曲率上界与肩的实际费用分开。marker幅度本分支为2e−5，三固定圆中心/半径不改。新增中心c_x=.58、镜面内c_z=.58tanγ，支撑目标.085、速度平方下限.18及全部权重在参数逐字保。既不借R740水平旧场全像界，也不借36初场的数值。

## 必要父输入的公开完整重生与身份

37实际先读取36中04/05两**完整系数场**在109×512网格的新规范读数。两个原始stage在已结束runner，故同一公开job以36原完整科学程序和原参数运行全部八阶段及三相几何，仅作为必要输入重生。原36终态38615B中的完整summary值按原JSON格式逐字还原，核原19068B/SHA256 ee4a781d8fd5a530335acc78543ade26ac6c3ae89edaedb5a044a9fc619063d1，保其原始来源。新replay自己的时钟、八阶段返回、full summary和stdout独立保，不把旧时钟当新实际测量。

必须核04完整NPZ2662B/SHA256 902b45b725e439eae5fc843a500cf7e18eaa0443665850e53a604c1879d9d1f9、266维坐标01f6797f491fe6f0d238902844366e84efcb1aa882b1526f2f2e0c0b1305e949；05完整NPZ3462B/SHA256 f719582f0c12a4f1eca9d7689cd6ddb873520d5ce69ec147883bda46fe055d8e、366维坐标df0c4a3bb6551f659cff9c544cb9e007b0f6e8de3be2adb78916ab9ad8a6eb17。完整container及真实little-endian C序坐标各自核对，若不同就记录真实差异，不把不同点冒同原输入。

## 公开运行与仍未支付的完成责任

科学源、六个输入全文均冻结实际触发commit的detached工作树。公共4CPU/16GB，Python3.12.14、NumPy2.3.5、SciPy1.17.0、单线程环境与36一致。360分钟是单job窗口，未加科学子进程墙钟截止；八秒观察、阶段立即发布、180秒完整小进度，至少每2700秒及每次发布前真实pull/rebase核双README，NFF立即重拉重推。原raw、NPZ与全stdout只在runner，公开小终态保完整身份和各实际返回。

三组后期场均按原13×56网格生成整闭像三相点云并作全部有序弦/直径/整云Hausdorff。此几何只量像集；实际按新规范同材料相位的C²逆角实现、全角误差、全径向误差、两端准确SVD规范、真正全时嵌入/reach及含反射欧氏商仍须同场支付。冻结640角函数的准确正性及工作评价误差不能靠有限节点成功代替。全部原README条件与机器/原容差真精化未付前继续求解，RC0和样本比值不作达标结论。

## 2026-11-28 12:35:41 UTC — 37 全部八新阶段自然结束与同目标两格实际失败

官方run46142745238/1与job140972094276均completed/success；trigger/source 30a3a01f4fc249b44d7c63ed58db0aaa7b7bf600，新真实child PID2840，2026-11-28T12:06:00Z至2026-11-28T12:21:44Z，RC0。完整源参/命令实际绑定见原终态。

原36八阶段完整必要重生RC0，未减预算，04/05完整NPZ及每个系数字均与原对象一致。原summary字节精确恢复19068B/ee4a781d8fd5a530335acc78543ade26ac6c3ae89edaedb5a044a9fc619063d1；重生summary19067B/cd3215e18eec3a8a844238383ebb034483e60e0774169857aa905327fb26cb5f。新stage0 tilt44-lift-parent05被选择；stage5一次冻结640角函数并保全部source/target SHA。

新八阶段自然完成，用时933.3894818079999秒。两固定g独立误差.917120251188229→.670383394669527，采样K9979.338755307148→2631.295839389866；这只是一次下降，离1e−6甚远。末场训练误差.07238775700019806与独立.670383394669527明显不同，不隐去密格代价。所有旧R740几何证书不自动传给投影或优化场。最后真实点b22c17b461dab8ad0f6630e89f42928cb83552c24b8cc6f2a9786efe8c9043ba。

同一目标定义、全部新阶段、全独立指标及返回的全三相点云如下。点云D/held/弦是有限样本，未付连续嵌入/reach/握持/含反射商距/全时同g或真正误差收敛。38已另外从原实际六jet求解，不重复这条已登记失败。

```json
{
  "summary_file": {
    "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/summary.json",
    "bytes": 20763,
    "sha256": "60ae3ce8d75864db1af54ce82aa6dea9ae5a42acf86ebcdce1fce0fde4daae5f"
  },
  "status": "completed_parent_comparison_design_and_two_frozen_resolutions",
  "elapsed": 933.3894818079999,
  "frozen_target": {
    "angular_count": 640,
    "check_257x2_sha256": "61edde029e9dda13a99db76d5f13d43416cbd79e5a0c8e2d41174454816feed3",
    "definition": "The same source field's fixed uniform-angle mean normal-speed-squared and mean angular speed at every requested physical radius. No radial interpolation. Target diag(E,P^2); physical s=L t.",
    "source_stage": 5,
    "source_x_sha256": "52951c2a3abd4c44aaa15a85dcda80f0b6baec3b45d7734231bb8d29f5dcb1c4"
  },
  "stages": [
    {
      "stage": 0,
      "design": "tilt44-lift-parent05",
      "x_sha256": "44920082dcfb6c43f26393c26622b5ab5e698b376018dda7d7814fd356ce8c6d",
      "coefficient_count": 202,
      "nfev": 90,
      "njev": 74,
      "configuration": {
        "angular": 96,
        "check_angular": 384,
        "check_radial": 61,
        "id": "arc-design-1",
        "lsmr_iterations": 100,
        "max_evaluations": 90,
        "mode": 10,
        "radial": 25,
        "regularizer": 0.000008,
        "spans": 6
      },
      "independent": {
        "K_sample_max": 503.28530362167567,
        "arclength_cross_speed_max": 0.1183128833700442,
        "gauged_max_relative": 0.726552112207967,
        "gauged_rms": 0.05453900421107042,
        "min_angular_speed": 0.19488669752275517,
        "min_projected_speed_squared": 0.01066791049603489,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 0.5999788770890193,
        "origin_radius_sample_max": 1.3900522951783036,
        "original_coordinate_gram_max": 7.511856862223752,
        "p0_relative_max": 0
      },
      "minimum_support": 0.04010480146057381,
      "frozen_target_source_x_sha256": null,
      "whole_sampled_phases": null
    },
    {
      "stage": 1,
      "design": "tilt32-parent04",
      "x_sha256": "f7b88942d01a056bf07fc143c56dd5b0f7e1ca3a068b60fb2eed69653ada8f14",
      "coefficient_count": 202,
      "nfev": 90,
      "njev": 74,
      "configuration": {
        "angular": 96,
        "check_angular": 384,
        "check_radial": 61,
        "id": "arc-design-1",
        "lsmr_iterations": 100,
        "max_evaluations": 90,
        "mode": 10,
        "radial": 25,
        "regularizer": 0.000008,
        "spans": 6
      },
      "independent": {
        "K_sample_max": 610.5287939222801,
        "arclength_cross_speed_max": 0.179310622337777,
        "gauged_max_relative": 0.6585608552862932,
        "gauged_rms": 0.06642496316725546,
        "min_angular_speed": 0.0837369470016904,
        "min_projected_speed_squared": 0.011123967292332842,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 0.6938551056023234,
        "origin_radius_sample_max": 1.3938531750071053,
        "original_coordinate_gram_max": 9.099650465742602,
        "p0_relative_max": 0
      },
      "minimum_support": 0.03235795223050464,
      "frozen_target_source_x_sha256": null,
      "whole_sampled_phases": null
    },
    {
      "stage": 2,
      "design": "tilt38-native",
      "x_sha256": "f6c4ff44bddd4e753ca33bb598cf4d79d45dc928b1fa5f1568b8ee88419efe47",
      "coefficient_count": 202,
      "nfev": 90,
      "njev": 79,
      "configuration": {
        "angular": 96,
        "check_angular": 384,
        "check_radial": 61,
        "id": "arc-design-1",
        "lsmr_iterations": 100,
        "max_evaluations": 90,
        "mode": 10,
        "radial": 25,
        "regularizer": 0.000008,
        "spans": 6
      },
      "independent": {
        "K_sample_max": 12293.908032407759,
        "arclength_cross_speed_max": 0.18635648834091417,
        "gauged_max_relative": 1.0513140663603835,
        "gauged_rms": 0.1039863431646397,
        "min_angular_speed": 0.09025177355220318,
        "min_projected_speed_squared": 0.0012265023321454988,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 0.5029463301010533,
        "origin_radius_sample_max": 1.3913463230484187,
        "original_coordinate_gram_max": 23.696658009504574,
        "p0_relative_max": 0
      },
      "minimum_support": 0.04143645918973518,
      "frozen_target_source_x_sha256": null,
      "whole_sampled_phases": null
    },
    {
      "stage": 3,
      "design": "horizontal-r740-ellipse",
      "x_sha256": "b9e790d452a86bce2b992c95f85858ebb9f4bbb6ed6c011dba059a621c2e60c2",
      "coefficient_count": 202,
      "nfev": 80,
      "njev": 51,
      "configuration": {
        "angular": 96,
        "check_angular": 384,
        "check_radial": 61,
        "id": "arc-design-1",
        "lsmr_iterations": 100,
        "max_evaluations": 90,
        "mode": 10,
        "radial": 25,
        "regularizer": 0.000008,
        "spans": 6
      },
      "independent": {
        "K_sample_max": 12519.863345528633,
        "arclength_cross_speed_max": 0.6367244314984689,
        "gauged_max_relative": 4.859081606036521,
        "gauged_rms": 0.25488387703200177,
        "min_angular_speed": 0.003686027132154634,
        "min_projected_speed_squared": 0.0019840931323420173,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 3.036515523405411,
        "origin_radius_sample_max": 1.4113653367613057,
        "original_coordinate_gram_max": 23.735859918646284,
        "p0_relative_max": 0
      },
      "minimum_support": -0.04523672836878079,
      "frozen_target_source_x_sha256": null,
      "whole_sampled_phases": null
    },
    {
      "stage": 4,
      "design": "tilt44-lift-parent05",
      "x_sha256": "b2fe7b79618acdacddf48560a445b73ea043d384f0e491e09b8466ada6d47e23",
      "coefficient_count": 454,
      "nfev": 100,
      "njev": 89,
      "configuration": {
        "angular": 144,
        "check_angular": 512,
        "check_radial": 83,
        "id": "arc-design-2",
        "lsmr_iterations": 120,
        "max_evaluations": 100,
        "mode": 14,
        "radial": 37,
        "regularizer": 0.000003,
        "spans": 10
      },
      "independent": {
        "K_sample_max": 323.08595511502205,
        "arclength_cross_speed_max": 0.14582882821511411,
        "gauged_max_relative": 0.4225328645475419,
        "gauged_rms": 0.02808169906458714,
        "min_angular_speed": 0.10788330347509963,
        "min_projected_speed_squared": 0.023449808754827075,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 0.840304091795506,
        "origin_radius_sample_max": 1.384125734469351,
        "original_coordinate_gram_max": 16.237206058371104,
        "p0_relative_max": 0
      },
      "minimum_support": 0.03729799173617332,
      "frozen_target_source_x_sha256": null,
      "whole_sampled_phases": null
    },
    {
      "stage": 5,
      "design": "tilt44-lift-parent05",
      "x_sha256": "52951c2a3abd4c44aaa15a85dcda80f0b6baec3b45d7734231bb8d29f5dcb1c4",
      "coefficient_count": 690,
      "nfev": 100,
      "njev": 92,
      "configuration": {
        "angular": 192,
        "check_angular": 640,
        "check_radial": 101,
        "id": "arc-design-3",
        "lsmr_iterations": 150,
        "max_evaluations": 100,
        "mode": 18,
        "radial": 45,
        "regularizer": 0.000001,
        "spans": 12
      },
      "independent": {
        "K_sample_max": 514.9506679688095,
        "arclength_cross_speed_max": 0.22187572336772998,
        "gauged_max_relative": 0.359765203757787,
        "gauged_rms": 0.020160796912988253,
        "min_angular_speed": 0.08749630140276948,
        "min_projected_speed_squared": 0.0305319393281089,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 1.493526724451371,
        "origin_radius_sample_max": 1.3809426565137737,
        "original_coordinate_gram_max": 29.47710992076481,
        "p0_relative_max": 0
      },
      "minimum_support": 0.052177110524406045,
      "frozen_target_source_x_sha256": null,
      "whole_sampled_phases": [
        {
          "phase": 0,
          "point_count": 2829,
          "sample_Hausdorff": 0,
          "sample_chord_inverse_reach_max": 74.76925347945784,
          "sample_diameter": 2.6634845275964647,
          "sample_witness_distance": 0.004999999999999893
        },
        {
          "phase": 1.5707963267948966,
          "point_count": 2829,
          "sample_Hausdorff": 0.7649483177498695,
          "sample_chord_inverse_reach_max": 74.76925347945784,
          "sample_diameter": 2.6634845275964647,
          "sample_witness_distance": 0.4649679931210999
        },
        {
          "phase": 3.141592653589793,
          "point_count": 2829,
          "sample_Hausdorff": 0.8192052879635289,
          "sample_chord_inverse_reach_max": 74.76925347945784,
          "sample_diameter": 2.6634845275964647,
          "sample_witness_distance": 0.5974697916097655
        }
      ]
    },
    {
      "stage": 6,
      "design": "tilt44-lift-parent05",
      "x_sha256": "c058fa553d281f67dcc79b10664f990ed67463bc8a003c0466c7e45f349391b4",
      "coefficient_count": 764,
      "nfev": 110,
      "njev": 105,
      "configuration": {
        "angular": 192,
        "check_angular": 640,
        "check_radial": 109,
        "id": "arc-frozen-1",
        "lsmr_iterations": 160,
        "max_evaluations": 110,
        "mode": 20,
        "radial": 49,
        "regularizer": 5e-7,
        "spans": 12
      },
      "independent": {
        "K_sample_max": 9979.338755307148,
        "arclength_cross_speed_max": 0.2255746212874794,
        "gauged_max_relative": 0.917120251188229,
        "gauged_rms": 0.04968830205980493,
        "min_angular_speed": 0.08640827287124772,
        "min_projected_speed_squared": 0.0013393198197171339,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 1.3623786809738547,
        "origin_radius_sample_max": 1.3816586181481167,
        "original_coordinate_gram_max": 27.691592891688245,
        "p0_relative_max": 0.002251796192957123
      },
      "minimum_support": 0.07228948513704048,
      "frozen_target_source_x_sha256": "52951c2a3abd4c44aaa15a85dcda80f0b6baec3b45d7734231bb8d29f5dcb1c4",
      "whole_sampled_phases": [
        {
          "phase": 0,
          "point_count": 2829,
          "sample_Hausdorff": 0,
          "sample_chord_inverse_reach_max": 64.19478777466423,
          "sample_diameter": 2.661848516722853,
          "sample_witness_distance": 0.004999999999999893
        },
        {
          "phase": 1.5707963267948966,
          "point_count": 2829,
          "sample_Hausdorff": 0.7747161656948336,
          "sample_chord_inverse_reach_max": 64.19478777466423,
          "sample_diameter": 2.661848516722853,
          "sample_witness_distance": 0.46427580489738923
        },
        {
          "phase": 3.141592653589793,
          "point_count": 2829,
          "sample_Hausdorff": 0.8179880733665433,
          "sample_chord_inverse_reach_max": 64.19478777466423,
          "sample_diameter": 2.661848516722853,
          "sample_witness_distance": 0.5974697916097655
        }
      ]
    },
    {
      "stage": 7,
      "design": "tilt44-lift-parent05",
      "x_sha256": "b22c17b461dab8ad0f6630e89f42928cb83552c24b8cc6f2a9786efe8c9043ba",
      "coefficient_count": 1356,
      "nfev": 120,
      "njev": 96,
      "configuration": {
        "angular": 256,
        "check_angular": 768,
        "check_radial": 131,
        "id": "arc-frozen-2",
        "lsmr_iterations": 180,
        "max_evaluations": 120,
        "mode": 24,
        "radial": 61,
        "regularizer": 2e-7,
        "spans": 18
      },
      "independent": {
        "K_sample_max": 2631.295839389866,
        "arclength_cross_speed_max": 0.13909380508156977,
        "gauged_max_relative": 0.670383394669527,
        "gauged_rms": 0.03449140601402816,
        "min_angular_speed": 0.08436135305239223,
        "min_projected_speed_squared": 0.004291833755331814,
        "min_signed_equator_height": 0,
        "normal_speed_angular_scatter_max": 1.2779785720144865,
        "origin_radius_sample_max": 1.379960886852057,
        "original_coordinate_gram_max": 31.678306323608865,
        "p0_relative_max": 0.00429022693876191
      },
      "minimum_support": 0.05778417545681647,
      "frozen_target_source_x_sha256": "52951c2a3abd4c44aaa15a85dcda80f0b6baec3b45d7734231bb8d29f5dcb1c4",
      "whole_sampled_phases": [
        {
          "phase": 0,
          "point_count": 2829,
          "sample_Hausdorff": 0,
          "sample_chord_inverse_reach_max": 51.745153724662195,
          "sample_diameter": 2.6573708941538112,
          "sample_witness_distance": 0.004999999999999893
        },
        {
          "phase": 1.5707963267948966,
          "point_count": 2829,
          "sample_Hausdorff": 0.7699146227075301,
          "sample_chord_inverse_reach_max": 51.7451537246622,
          "sample_diameter": 2.6573708941538112,
          "sample_witness_distance": 0.46381523585155493
        },
        {
          "phase": 3.141592653589793,
          "point_count": 2829,
          "sample_Hausdorff": 0.8144295399536794,
          "sample_chord_inverse_reach_max": 51.7451537246622,
          "sample_diameter": 2.6573708941538112,
          "sample_witness_distance": 0.5974697916097655
        }
      ]
    }
  ],
  "whole_runner_field_files": {
    "complete_inventory": {
      "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/complete-field-file-inventory.json",
      "bytes": 1873,
      "sha256": "fc59a2c694ba8029b29b1dcc705094655d5bfa49555f6c8a903807c540f85e18"
    },
    "original_file_count": 9,
    "complete_file_records": [
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/current-field.npz",
        "bytes": 11126,
        "sha256": "f019e708445ea7cf0deb27ee77c8039ea82bee7b9832f382e6356bfa38951e33"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-00.npz",
        "bytes": 1894,
        "sha256": "3d63d361128eafd9e163320818565cd47cb81e2bdefdc9db33e21fa350943652"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-01.npz",
        "bytes": 1894,
        "sha256": "69b3a19290f26e7ef18fb26b09303e8a1fef7c84f938fa603750ff81d21ca93d"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-02.npz",
        "bytes": 1894,
        "sha256": "fbf7df4c62a7cec5d5a6ba76c8da3e106490c674ae8ae140119720f3b22d60d7"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-03.npz",
        "bytes": 1894,
        "sha256": "095380066f21710a4e779c88908a31b1434015978a2f9a3f82f3978124505ec1"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-04.npz",
        "bytes": 3910,
        "sha256": "9565c7820efc237dc808f30ff0c00d78849ab1ea246886f2809973c08ef01062"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-05.npz",
        "bytes": 5798,
        "sha256": "5710401acdb0456389d261b4eefa645b203fce0240dc1680e0c01a2c33cb62fe"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-06.npz",
        "bytes": 6390,
        "sha256": "2f4c1b5addfb138d089a0f8d306da9da4d31b1b1777961557020f152da8b6ae6"
      },
      {
        "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/field/stage-07.npz",
        "bytes": 11126,
        "sha256": "ff2cb1bb158913c9dc681f7d27dad56415fb5e465b70babe03468206d059f76c"
      }
    ],
    "best_field_records": []
  },
  "stdout_stderr": {
    "path": "/home/runner/work/_temp/run37-bent-disk-arclength-46142745238-1/complete-scientific-stdout-stderr.log",
    "bytes": 8046,
    "sha256": "50df21b33c8390ff4ce2008d25cc8ede2442a4adae1942748d42906b9f9cbca9"
  }
}
```


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/run37-bent-disk-arclength-46142745238-1.json",
    "bytes": 50458,
    "sha256": "3f617daca5e28b3d2bc1fb7f36f187f95ce7e916a9676d702b8c54e0c91977d8",
    "git_blob_sha": "197f2a51e61312558c54663c1a0c3c9c191e734b",
    "fixed_commit": "78431ea8c1989f7e47fb9bed4c02d9d572b7d1d4",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```
